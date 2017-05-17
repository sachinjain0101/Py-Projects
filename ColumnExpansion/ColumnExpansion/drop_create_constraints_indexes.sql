/*
USE TimeHistory;
GO

DROP TABLE zzzSACHINJAIN;
GO

CREATE TABLE zzzSACHINJAIN( id1 INT, id2 INT);
ALTER TABLE zzzSACHINJAIN ALTER COLUMN id1 INT NOT NULL;
ALTER TABLE zzzSACHINJAIN ALTER COLUMN id2 INT NOT NULL;
ALTER TABLE zzzSACHINJAIN ADD CONSTRAINT pk_zzzSACHINJAIN_PK PRIMARY KEY(id1, id2);
GO

ALTER TABLE zzzSACHINJAIN ADD x0 INT NULL;
ALTER TABLE zzzSACHINJAIN ADD x1 INT NOT NULL;
ALTER TABLE zzzSACHINJAIN ADD CONSTRAINT uq_zzzSACHINJAIN_1 UNIQUE(id1,x0)
ALTER TABLE zzzSACHINJAIN ADD CONSTRAINT uq_zzzSACHINJAIN_2 UNIQUE(x1);
GO 
ALTER TABLE zzzSACHINJAIN ADD x2 INT;
ALTER TABLE zzzSACHINJAIN ADD x3 INT;
ALTER TABLE zzzSACHINJAIN ADD x4 INT DEFAULT 0;
ALTER TABLE zzzSACHINJAIN ADD x5 INT CHECK (x5 > 0 AND x5 < 9999);
ALTER TABLE zzzSACHINJAIN ADD x6 INT DEFAULT 0;

CREATE NONCLUSTERED INDEX idx1_nc ON zzzSACHINJAIN (x0, x1 DESC);
CREATE NONCLUSTERED INDEX idx2_nc ON zzzSACHINJAIN (x2 DESC) INCLUDE (x4);
CREATE NONCLUSTERED INDEX idx3_nc ON zzzSACHINJAIN (x3) INCLUDE (x5,x6) WITH (FILLFACTOR=90);
GO

INSERT INTO zzzSACHINJAIN VALUES( 1, 1, 1, 1, 1, 1, 1, 1,1);
INSERT INTO zzzSACHINJAIN VALUES( 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000);
INSERT INTO zzzSACHINJAIN VALUES( 1111, 1111, 1111, 1111, 1111, 1111, 1111, 1111, 1111);
*/

WITH ZZZ AS
(
SELECT DISTINCT
       'DROP INDEX '+i.name+' on '+OBJECT_NAME(i.object_id)+';' AS DROP_IDX
	  , 'CREATE '+i.type_desc+' INDEX '+i.name COLLATE SQL_Latin1_General_CP437_CI_AS +' ON '+OBJECT_NAME(i.object_id)
	  + '('
	  + COALESCE(STUFF(( SELECT ','+'['+COL_NAME(XX.object_id, XX.column_id)+'] '+ CASE WHEN XX.is_descending_key = 1 THEN 'DESC' ELSE '' END
					  FROM sys.index_columns AS XX
					  WHERE XX.object_id = i.object_id
					  AND XX.index_id = i.index_id AND XX.is_included_column = 0 ORDER BY ic.key_ordinal FOR XML PATH('')
				   ), 1, 1, '')
			  ,'')
       + ') ' AS MAIN_STR
	  , 'INCLUDE ('
	  + COALESCE(STUFF(( SELECT ','+'['+COL_NAME(XX.object_id, XX.column_id)+']'
					  FROM sys.index_columns AS XX
					  WHERE XX.object_id = i.object_id
					  AND XX.index_id = i.index_id AND XX.is_included_column = 1 ORDER BY ic.key_ordinal FOR XML PATH('')
				   ), 1, 1, '')
			 ,'')
	  + ') ' AS INCLUDE_STR
	  , 'WITH ('
	  + 'PAD_INDEX = '+ CASE WHEN is_padded=0 THEN 'OFF' ELSE 'ON' END
	  + ', STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF'
	  + ', ALLOW_ROW_LOCKS = '+ CASE WHEN allow_row_locks=0 THEN 'OFF' ELSE 'ON' END 
	  + ', ALLOW_PAGE_LOCKS = '+ CASE WHEN allow_page_locks=0 THEN 'OFF' ELSE 'ON' END 
	  + ', IGNORE_DUP_KEY = '+ CASE WHEN ignore_dup_key = 0 THEN 'OFF' ELSE 'ON' END
	  +  CASE WHEN fill_factor = 0 THEN '' ELSE ', FILLFACTOR = '+ CAST(fill_factor AS VARCHAR(3)) END
	  + ')' AS WITH_STR
FROM sys.indexes AS i
INNER JOIN sys.index_columns AS ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
WHERE 1=1
	 AND is_primary_key = 0 AND is_unique_constraint = 0
	 AND i.object_id = OBJECT_ID('zzzSACHINJAIN') 
)
--*********************************************************************
--DROP INDEXES
--*********************************************************************
SELECT
DROP_IDX
FROM ZZZ
UNION ALL
--*********************************************************************
--DROP PK AND UNIQUE CONSTRAINTS
--*********************************************************************
SELECT
DISTINCT 'ALTER TABLE ' + TC.TABLE_SCHEMA + '.' + tc.TABLE_NAME + ' DROP CONSTRAINT ' + TC.CONSTRAINT_NAME + ';' AS DROP_CONSTRAINT
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
JOIN INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE cc ON tc.Constraint_Name = cc.Constraint_Name
WHERE 1=1
AND tc.CONSTRAINT_TYPE IN ('PRIMARY KEY','UNIQUE')
AND tc.TABLE_NAME = 'zzzSACHINJAIN'
UNION ALL
--*********************************************************************
--DROP CHECK CONSTRAINTS
--*********************************************************************
SELECT DISTINCT
'ALTER TABLE ' + SCHEMA_NAME(t.schema_id)+'.' + t.name + ' DROP CONSTRAINT ' + dc.name + ';' AS DROP_CONSTRAINT
FROM sys.all_columns AS c
     INNER JOIN sys.tables AS t ON c.object_id = t.object_id
     INNER JOIN sys.check_constraints AS dc ON T.object_id = DC.parent_object_id
WHERE 1 = 1
      AND t.name = 'zzzSACHINJAIN'
UNION ALL
--*********************************************************************
--DROP DEFAULT CONSTRAINTS
--*********************************************************************
SELECT DISTINCT 'ALTER TABLE ' + SCHEMA_NAME(t.schema_id)+'.' + t.name+' DROP CONSTRAINT '+dc.name+';' AS DROP_CONSTRAINT
FROM sys.all_columns AS c
     INNER JOIN sys.tables AS t ON c.object_id = t.object_id
     INNER JOIN sys.default_constraints AS dc ON c.default_object_id = dc.object_id
WHERE 1 = 1
      AND t.name = 'zzzSACHINJAIN'
UNION ALL
--*********************************************************************
--ADD PK AND UNIQUE CONSTRAINTS
--*********************************************************************
SELECT
DISTINCT 'ALTER TABLE ' + TC.TABLE_SCHEMA + '.' + tc.TABLE_NAME
       + ' ADD CONSTRAINT '+TC.CONSTRAINT_NAME+' '+TC.CONSTRAINT_TYPE
       + '('+ COALESCE(STUFF((SELECT ','+cc.COLUMN_NAME
	   				     FROM INFORMATION_SCHEMA.constraint_column_usage cc
					     WHERE tc.Constraint_Name = cc.Constraint_Name
					     ORDER BY cc.COLUMN_NAME FOR XML PATH('')
				        ), 1, 1, '')
				  ,'')
       + ');' AS ADD_CONSTRAINT
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
JOIN INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE cc ON tc.Constraint_Name = cc.Constraint_Name
WHERE 1=1
AND tc.CONSTRAINT_TYPE IN ('PRIMARY KEY','UNIQUE')
AND tc.TABLE_NAME = 'zzzSACHINJAIN'
UNION ALL
--*********************************************************************
--ADD CHECK CONSTRAINTS
--*********************************************************************
SELECT DISTINCT
'ALTER TABLE ' + SCHEMA_NAME(t.schema_id)+'.' + t.name + ' ADD CONSTRAINT ' + dc.name + ' CHECK ' + dc.definition+';'  AS CREATE_CONSTRAINT
FROM sys.all_columns AS c
     INNER JOIN sys.tables AS t ON c.object_id = t.object_id
     INNER JOIN sys.check_constraints AS dc ON T.object_id = DC.parent_object_id
WHERE 1 = 1
      AND t.name = 'zzzSACHINJAIN'
UNION ALL
--*********************************************************************
--ADD DEFAULT CONSTRAINTS
--*********************************************************************
SELECT DISTINCT 'ALTER TABLE ' + SCHEMA_NAME(t.schema_id)+'.' + t.name+' ADD CONSTRAINT '+dc.name+' DEFAULT '+dc.definition+' FOR '+c.name+';' AS CRAETE_CONSTRAINT
FROM sys.all_columns AS c
     INNER JOIN sys.tables AS t ON c.object_id = t.object_id
     INNER JOIN sys.default_constraints AS dc ON c.default_object_id = dc.object_id
WHERE 1 = 1
      AND t.name = 'zzzSACHINJAIN'
UNION ALL
--*********************************************************************
--CREATE INDEXES
--*********************************************************************
SELECT
CASE WHEN INCLUDE_STR = 'INCLUDE () ' THEN MAIN_STR + WITH_STR + ';' ELSE MAIN_STR + INCLUDE_STR + WITH_STR + ';' END AS CREATE_IDX
FROM ZZZ
;


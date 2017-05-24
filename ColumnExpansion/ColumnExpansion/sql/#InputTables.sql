DECLARE @tableName VARCHAR(100);
DECLARE @columnName VARCHAR(100);
DECLARE @stmt VARCHAR(1000);

IF OBJECT_ID('tempdb..#InputTables') IS NOT NULL
BEGIN
    PRINT 'Dropping #InputTables'
    DROP TABLE #InputTables;
END;

CREATE TABLE #InputTables (Id INT IDENTITY(1, 1), ColumnName VARCHAR(100), TableName  VARCHAR(100));

--Inserting TimeCurrent Tables	
INSERT INTO #InputTables(ColumnName, TableName) 
Values 	
--('AprvlAdjOrigRecID',	'tblTimeHistDetail'),
('THDRecordID',	'tblKronosPunchExport'),
('THDRecordID',	'tblKronosPunchExport_Audit'),
('THDRecordID',	'tblStaffingApproval_THD'),
('THDRecordID',	'tblTimeHistDetail_BackupApproval'),
('THDRecordID',	'tblTimeHistDetail_PATE'),
('THDRecordID',	'tblTimeHistDetail_UDF'),
('THDRecordID',	'tblWork_KronosExport'),
('OrigRecordID','tblFixPunchAudit'),
('FromRecordID','tblTimeHistDetail_Crossover'),
('ToRecordID','tblTimeHistDetail_Crossover'),
('DetailRecordID','tblTimeHistDetail_Disputes'),
('THD_RecordId','tblTimeHistDetail_Faxaroo'),
('AdjustmentRecordID','tblTimeHistDetail_Reasons'),
('RecordID','tblTimeHistDetail_Partial'),
('AprvlAdjOrigRecID','tblTimeHistDetail_Partial'),
('RecordId','tblFixedPunchByEE'),
('InOutId','tblWTE_Spreadsheet_Breaks'),
--('ClkTransNo','tblTimeHistDetail'),
--('RecordId','tblTimeHistDetail'),
('RecordId','tblWork_TimeHistDetail'),
('RecordId','Extract_Hashbytes_MatchingTable'),
--('JobId','tblTimeHistDetail'),
('RecordId','tblSTAFRevman_Extract'),	
('RecordId','tblEmplMissingPuncgReceipt'),	
('ClkTransNo','tblTimeHistDetail_Partial'),	
--('DivisionId','tblTimeHistDetail'),	
('DivisionId','tblTimeHistDetail_Partial');

INSERT INTO #InputTables(ColumnName, TableName) 
Values 	
--('SiteNo','tblTimeHistDetail'),
('SiteNo',	'zzJimResearch_TimeHistDetail'),
('SiteNo',	'tblEmplShifts'),
('SiteNo',	'tblTimeCards_Control_DELETE'),
('SiteWorkedAt','tblGambroUploads'),
('HomeSite','tblGambroUploads'),
('SiteChargedTo','tblGambroUploads'),
('SiteNo',	'tblAdjustments'),
('SiteNo',	'tblTimeHistDetail_ZeroSite'),
--('SiteNo','tblDeptNames'),
--('SiteNo','tblEmplSites_Depts'),
('SiteNo',	'tblEmplClass'),
('SiteNo',	'tblWork_TimeHistDetail'),
--('SiteNo','tblEmplSites'),
('SiteNo',	'tblWTE_Project_Archive'),
('SiteNo'	,'OLSTLegal'),
('InSite',	'tblPunchImport'),
('OutSite','tblPunchImport'),
('SiteNo',	'tblImportLog'),
('SiteNo',	'tblTimeHistDetail_Orig'),
('SiteNo',	'tblTimeHistDetail_GeoLocation'),
--('SiteNo','tblSiteNames'),
('SiteNo',	'tblTimeHistDetail_backup'),
('SiteNo',	'tblTimeHistDetail_COAS_pre'),
('SiteNo',	'tblDataFormStatus'),
('SiteNo',	'VANGlegal'),
('SiteNo',	'tblTimeHistDetail_Partial'),
('SiteNo',	'tblDataFormValues'),
('SiteNo',	'tblWork_TimeHistDetail2'),
('PrimarySite',	'tblEmplNames'),
('SiteNo',	'tblFixPunchAudit'),
('siteno',	'STFMCompassBank'),
('WorkedSiteNo','tblCIAHistory_DAVT'),
('PrimarySiteNo','tblCIAHistory_DAVT'),
('SiteNo',	'tblStdJobs'),
('SiteNo',	'tblStdJobs_Audit'),
('SiteNo',	'tblTimeHistDetail_DELETED'),
('SiteNo',	'ADVOlegal'),
('SiteNo',	'tblTimeCards_DELETE'),
('SiteNo',	'tblStdJobCellEmployees'),
('SiteNo',	'tblTimeHistDetail_COAS_post'),
('SiteNo',	'tblExpenseLineItems');

INSERT INTO #InputTables(ColumnName, TableName) 
Values 	
--('DeptNo',	'tblTimeHistDetail'),
('DeptNo',	'zzJimResearch_TimeHistDetail'),
('DeptNo',	'tblEmplShifts'),
('DeptNo',	'tblDeptShifts'),
('DeptNo',	'tblGambroUploads'),
('DeptNo',	'tblAdjustments'),
('DeptNo',	'tblTimeHistDetail_ZeroSite'),
--('DeptNo',	'tblDeptNames'),
--('DeptNo',	'tblEmplSites_Depts'),
('deptno',	'tblCOAS_Screwup'),
('deptno',	'tblCOAS_Screwup2'),
('DeptNo',	'tblWork_TimeHistDetail'),
--('Department','tblEmplNames_Depts'),
('PrimaryDept',	'OLSTLegal'),
('DeptNo',	'OLSTLegal'),
('DeptNo',	'tblPunchImport'),
('DeptNo',	'tblTimeHistDetail_Orig'),
('DeptNo',	'tblBudgetData'),
('DeptNo',	'tblTimeHistDetail_backup'),
('DeptNo',	'tblTimeHistDetail_COAS_pre'),
('PrimaryDept',	'VANGlegal'),
('DeptNo',	'VANGlegal'),
('DeptNo',	'tblTimeHistDetail_Partial'),
('DeptNo',	'tblWork_TimeHistDetail2'),
('DeptNo',	'tblFixPunchAudit'),
('deptno',	'STFMCompassBank'),
('newdept','STFMCompassBank'),
('DeptNo',	'tblStdJobs'),
('DeptNo',	'tblStdJobs_Audit'),
('DeptNo',	'tblTimeHistDetail_DELETED'),
('PrimaryDept',	'ADVOlegal'),
('DeptNo',	'ADVOlegal'),
('DeptNo',	'tblTimeHistDetail_COAS_post'),
('DeptNo',	'tblExpenseLineItems'),
('DeptNo', 'tblTimeCards_Control_DELETE'),
('DeptNo', 'tblTimeCards_DELETE');

DECLARE dbCur1 CURSOR LOCAL
FOR SELECT DISTINCT TableName from #InputTables;

BEGIN
    IF OBJECT_ID('tblColumnExpansionStmts') IS NOT NULL
    BEGIN
	   PRINT 'Dropping tblColumnExpansionStmts'
	   DROP TABLE tblColumnExpansionStmts;
    END;
    CREATE TABLE tblColumnExpansionStmts (ID int IDENTITY, Stmt VARCHAR(1000));


    OPEN dbCur1
    FETCH NEXT FROM dbCur1 INTO @tableName;
    WHILE @@FETCH_STATUS = 0   
    BEGIN
    	   PRINT 'Processing table '+@tableName;
	   IF OBJECT_ID('tempdb..#ZZZ') IS NOT NULL
	   BEGIN
	   	   PRINT 'Dropping #ZZZ'
		  DROP TABLE #ZZZ;
	   END;

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
			--+ ', IGNORE_DUP_KEY = '+ CASE WHEN ignore_dup_key = 0 THEN 'OFF' ELSE 'ON' END
			+  CASE WHEN fill_factor = 0 THEN '' ELSE ', FILLFACTOR = '+ CAST(fill_factor AS VARCHAR(3)) END
			+ ')' AS WITH_STR
			INTO #ZZZ
	   FROM sys.indexes AS i
	   INNER JOIN sys.index_columns AS ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
	   WHERE 1=1
		    AND is_primary_key = 0 AND is_unique_constraint = 0
		    AND i.object_id = OBJECT_ID(@tableName) 

	   INSERT INTO tblColumnExpansionStmts
	   SELECT * FROM 
	   (
		  --*********************************************************************
		  --DROP INDEXES
		  --*********************************************************************
		  SELECT
		  DROP_IDX
		  FROM #ZZZ
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
		  AND tc.TABLE_NAME = @tableName
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
			   AND t.name = @tableName
		  UNION ALL
		  --*********************************************************************
		  --DROP DEFAULT CONSTRAINTS
		  --*********************************************************************
		  SELECT DISTINCT 'ALTER TABLE ' + SCHEMA_NAME(t.schema_id)+'.' + t.name+' DROP CONSTRAINT '+dc.name+';' AS DROP_CONSTRAINT
		  FROM sys.all_columns AS c
			  INNER JOIN sys.tables AS t ON c.object_id = t.object_id
			  INNER JOIN sys.default_constraints AS dc ON c.default_object_id = dc.object_id
		  WHERE 1 = 1
			   AND t.name = @tableName
	   ) A
	   INSERT INTO tblColumnExpansionStmts VALUES ('GO');
	   SET @stmt = '';
	   INSERT INTO tblColumnExpansionStmts
	   SELECT 'DROP STATISTICS '+@tableName+'.'+ Name +';' FROM sys.stats WHERE object_id = object_id(@tableName)

	   INSERT INTO tblColumnExpansionStmts VALUES ('GO');

	   DECLARE dbCur2 CURSOR LOCAL
	   FOR SELECT ColumnName from #InputTables WHERE TableName = @tableName;
	   BEGIN
		  OPEN dbCur2
		  FETCH NEXT FROM dbCur2 INTO @columnName;
		  WHILE @@FETCH_STATUS = 0   
		  BEGIN
		  SET @stmt = '';
		  SELECT @stmt = 'ALTER TABLE '+@tableName+' ALTER COLUMN '+@columnName+
					   CASE WHEN (UPPER(@columnName) LIKE '%DEPT%' OR UPPER(@columnName) LIKE '%SITE%')
							 THEN ' INT' 
						   ELSE ' BIGINT'
					   END + CASE WHEN IS_NULLABLE = 'NO' THEN ' NOT NULL;' ELSE ';' END
		  FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = @tableName AND COLUMN_NAME = @columnName;
		  PRINT '>>>   '+@stmt
		  INSERT INTO tblColumnExpansionStmts VALUES (@stmt);
		  FETCH NEXT FROM dbCur2 INTO @columnName;   
		  END;
		  CLOSE dbCur2;
		  DEALLOCATE dbCur2;
	   END

	   INSERT INTO tblColumnExpansionStmts VALUES ('GO');
	   INSERT INTO tblColumnExpansionStmts
	   SELECT * FROM 
	   (
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
		  AND tc.TABLE_NAME = @tableName
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
			   AND t.name = @tableName
		  UNION ALL
		  --*********************************************************************
		  --ADD DEFAULT CONSTRAINTS
		  --*********************************************************************
		  SELECT DISTINCT 'ALTER TABLE ' + SCHEMA_NAME(t.schema_id)+'.' + t.name+' ADD CONSTRAINT '+dc.name+' DEFAULT '+dc.definition+' FOR '+c.name+';' AS CRAETE_CONSTRAINT
		  FROM sys.all_columns AS c
			  INNER JOIN sys.tables AS t ON c.object_id = t.object_id
			  INNER JOIN sys.default_constraints AS dc ON c.default_object_id = dc.object_id
		  WHERE 1 = 1
			   AND t.name = @tableName
		  UNION ALL
		  --*********************************************************************
		  --CREATE INDEXES
		  --*********************************************************************
		  SELECT
		  CASE WHEN INCLUDE_STR = 'INCLUDE () ' THEN MAIN_STR + WITH_STR + ';' ELSE MAIN_STR + INCLUDE_STR + WITH_STR + ';' END AS CREATE_IDX
		  FROM #ZZZ
	   ) A
	   INSERT INTO tblColumnExpansionStmts VALUES ('GO');
    FETCH NEXT FROM dbCur1 INTO @tableName;   
    END;
    CLOSE dbCur1;
    DEALLOCATE dbCur1;
    SELECT * FROM tblColumnExpansionStmts ORDER BY ID;

END

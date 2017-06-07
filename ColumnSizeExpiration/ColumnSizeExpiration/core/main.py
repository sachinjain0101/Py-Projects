from core import Vars
from core import getAppLogger

from sklearn import datasets, linear_model
import sqlalchemy
import urllib
import os
import pandas
import numpy
import time

class ColSizeExp(object):

    seltbls = """
              SELECT DISTINCT
                     DbName
                    ,SchName
                    ,TblName
                    ,MaxCount
              FROM Metrics.dbo.tbl_TableIdentityStats_New
              WHERE 1=1
              AND SchName IS NOT NULL
              ORDER BY 1,2,3
              """

    seldata = """
              SELECT (EpochTime/1000) - 432000000 AS X
                    ,DbName
                    ,SchName
                    ,TblName
                    ,ColName
                    ,TypName
                    ,MaxCount
                    ,COALESCE(CurrCount,0) AS Y
              FROM Metrics.dbo.tbl_TableIdentityStats_New
              WHERE TblName = '{0}'
              AND DbName = '{1}'
              ORDER BY DbName,TblName,CurrCount DESC
              """

    selmax = """
              SELECT MAX(COALESCE((EpochTime/1000) - 432000000,0)) AS MaxCount
              FROM Metrics.dbo.tbl_TableIdentityStats_New
              WHERE TblName = '{0}'
              AND DbName = '{1}'
              """
    logger=None
    
    def __init__(self):
        self.logger = getAppLogger(__name__)
        self.logger.info('object constructed')

    def fmtDict(self,out):
        lst = list()
        for k in out:
            lst.append('<tr> <td>'+k+'</td> <td>'+str(out.get(k))+'</td> </tr>')
        return lst

    def calcLinReg(self):
        out = dict()

        self.logger.info('start')
        self.logger.info('creating db engine')
        params = urllib.quote_plus(Vars.CONN_STR.format('l-9560-0101','Metrics'))
        engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={0}'.format(params))

        tables = pandas.DataFrame()
        with engine.connect() as conn, conn.begin():
            tables = pandas.read_sql_query(self.seltbls, engine)
            conn.close()

        for i,row in tables.iterrows():
            #self.logger.info(row['TblName']+' # '+str(row['MaxCount']))
            data = pandas.DataFrame()
            maxepochtime=0
            with engine.connect() as conn, conn.begin():
                data = pandas.read_sql_query(self.selmax.format(row['TblName'],row['DbName']), engine)
                conn.close()
            maxepochtime = data.MaxCount[0]         

            data=None
            with engine.connect() as conn, conn.begin():
                data = pandas.read_sql_query(self.seldata.format(row['TblName'],row['DbName']), engine)
                conn.close()

            datasize = len(data)
            #self.logger.info(datasize)

            matrix = data.as_matrix(['X','Y'])
            #self.logger.info(matrix)

            X = numpy.reshape(matrix[:,0],(datasize,1))
            #self.logger.info(X)
            Y = numpy.reshape(matrix[:,1],(datasize,1))
            #self.logger.info(Y)

            regr = linear_model.LinearRegression()
            regr.fit(X, Y)

            M=(regr.coef_)[0][0]
            B=(regr.intercept_)[0]

            #Y=MX+B
            #X=(Y-B)/M
            px=0.0
            if M==0:
                px=(row['MaxCount']-B)
            else:
                px=(row['MaxCount']-B)/M

            #self.logger.info('M: {0}'.format(M))
            #self.logger.info('B: {0}'.format(B))
            #self.logger.info('px: {0}'.format(px))

            daysremaining=(px-maxepochtime)/86400

            dt=''
            try:
                dt=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(px))
            except:
                dt='date to large'
                pass
            #self.logger.info(dt)
            out.update({row['DbName']+'.'+row['SchName']+'.'+row['TblName']:daysremaining})

        return out

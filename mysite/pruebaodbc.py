import pyodbc

print("hola")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=192.168.8.41;'
                      'UID=cti;'
                      'PWD=ctidb;'
                      'Database=ctidb_transact;')
                      #'Trusted_Connection=yes;')
                      #DSN=QadNet;UID=CGCOM;HOST=192.168.8.7;PORT=7120;DB=cstprod;

cursor = conn.cursor()
#cursor.execute('SELECT TOP (10) [TRANSACTIONINDEX], [PLANTID]  FROM [ctidb_transact].[dbo].[CONVERTPROD]')
cursor.execute('SELECT TOP (10) [TRANSACTIONINDEX] ,[ORDERID] ,[PARTID] FROM [ctidb_transact].[dbo].[ORDERS_INFO] order by transactionindex desc ')

for row in cursor:
    print(row)

print("adios")

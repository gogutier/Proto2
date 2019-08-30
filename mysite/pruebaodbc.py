from time import time, sleep
import pyodbc


print("hola")

def cargaDatos():
    print("conectándose a DB..")
    flag=0

    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=192.168.8.41;'
                              'UID=cti;'
                              'PWD=ctidb;'
                              'Database=ctidb_transact;')
                              #'Trusted_Connection=yes;')
                              #DSN=QadNet;UID=CGCOM;HOST=192.168.8.7;PORT=7120;DB=cstprod;

        cursor = conn.cursor()
        flag=1
        print("Conectado a DB :D")

    except:
        print("Error al conectarse a la DB!!")
        flag=0
        #cursor.execute('SELECT TOP (10) [TRANSACTIONINDEX], [PLANTID]  FROM [ctidb_transact].[dbo].[CONVERTPROD]')
    if flag==1:
        while True:
            try:
                print("iniciando consulta")

                cursor.execute('SELECT TOP (10) [TRANSACTIONINDEX],[ORDERID],[UNITTYPE],[LOADID],[UNITNO],[SOURCE],[DESTINATION],[EVENTDATETIME]  FROM [ctidb_transact].[dbo].[MVLOAD] order by transactionindex desc ')

                for row in cursor:
                    print(row)

                print("adios")
                sleep(10)
            except:
                print("Error!")
                break

    else:
        print("Oh, a ocurrido un error!")

while True:
    cargaDatos()
    sleep(2)

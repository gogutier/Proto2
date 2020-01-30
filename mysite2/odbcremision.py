from __future__ import print_function
import mechanicalsoup
import argparse
from getpass import getpass
from time import time, sleep
from datetime import datetime
import pyodbc
import sys



def cargaDatos(rem):

    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=192.168.8.41;'
                              'UID=cti;'
                              'PWD=ctidb;'
                              'Database=ctidb_transact;')
                              #'Trusted_Connection=yes;')
                              #DSN=QadNet;UID=CGCOM;HOST=192.168.8.7;PORT=7120;DB=cstprod;

        cursor = conn.cursor()
        print("Conectado a DB :D")





        print("conectándose a DB para encontrar la remisión " + str(rem))

        print("obteniendo el último Transact más cercano..")
        cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX],[BILLOFLADINGID],[TRUCKID],[SHIPTOCUSTOMERNAME],[ORDERID],[SPECID],[ITEMDESCRIPTION],[TRAILERID],[COMMENTS],[PCFLAG] FROM [ctidb_transact].[dbo].[BILLOFLADINGINFO]  where billofladingid="+ str(rem) + " order by transactionindex desc")
        if len(cursor.fetchall())>0:
            cursor.execute("SELECT TOP (1) [TRANSACTIONINDEX],[BILLOFLADINGID],[TRUCKID],[SHIPTOCUSTOMERNAME],[ORDERID],[SPECID],[ITEMDESCRIPTION],[TRAILERID],[COMMENTS],[PCFLAG] FROM [ctidb_transact].[dbo].[BILLOFLADINGINFO]  where billofladingid="+ str(rem) + " order by transactionindex desc")
            row0=cursor.fetchone()
            remi=[]
            for item in row0:
                remi.append(item)

            transact=row0[0]
            print(remi)
            print("Transact obtenido: " + str(transact))

            print("buscando datos de la remisión")
            cursor.execute("SELECT TOP (1000) [TRANSACTIONINDEX],[ORDERID],[UNITID],[UNITQTY],[SALESORDERNO],[LOCATION] FROM [ctidb_transact].[dbo].[BILLOFLADINGLOAD] where transactionindex="+ str(transact) +" order by transactionindex desc")
            pallets=cursor.fetchall()
            respuesta=[]
            for pallet in pallets:
                print(pallet)
                aux=[]
                for item in pallet:
                    aux.append(item)
                respuesta.append(aux)
            return(respuesta, remi)
        else:
            return([])

    except Exception as e:
        print(e)
        print("error al conectar con DB :(")
        return (["Error carga datos"])
    #print("row0 FGLOAD:")

    #return(row1, datosextra)

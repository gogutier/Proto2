from __future__ import print_function
import mechanicalsoup
import argparse
from getpass import getpass
from time import time, sleep
from datetime import datetime, timedelta
import pyodbc
import sys


def conecta_BD():
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
        return(cursor)

    except Exception as e:
        print(e)
        print("error al conectar con DB :(")

def consulta(datetimeini,datetimefin):

    ini=datetimeini.strftime("%Y-%m-%d %H:%M:%S")
    fin=datetimefin.strftime("%Y-%m-%d %H:%M:%S")


    m2totconvwaste=0
    m2totcorrwaste=0

    cursor= conecta_BD()
    #Saco el dato de conversión
    #Acá voy a considerar que la campaña completa se hace dentro del mismo turno en que comienza su runstartedate, para evitar el caso en que dejan el setup iniciado desde elfin del turno anterior.
    cursor.execute("SELECT TOP (3000)[WORKCENTERID],[ORDERID],[OPERATIONNO],[SETUPSTARTDATE],[SETUPENDDATE],[RUNSTARTDATE],[RUNENDDATE],[SETUPTOTAL],[RUNTOTAL],[GOODQUANTITY],[INPUTSHEETWIDTH],[INPUTSHEETLENGTH],[NUMBEROUT],[NUMBERIN],[REVIEWEDFLAG] FROM [ctidb_transact].[dbo].[CONVERTPROD] where SETUPSTARTDATE Between '"+ ini +"' And '"+ fin +"' order by transactionindex desc")
    #row0=cursor.fetchone()
    m2totconv=0
    m2totconvwaste=0
    for row in cursor.fetchall():
        if (row[0]=="TCY" or row[0]=="HCR" or row[0]=="WRD" or row[0]=="FFW" or row[0]=="DRO" or row[0]=="FFG"):# or row[0]=="DIM" or row[0]=="TAB"):
            m2placa=row[10]*row[11]
            unids=row[9]/row[12]
            unidsmalas=(row[8]-row[9])/row[12]

            m2prod=m2placa*unids
            m2prodmala=m2placa*unidsmalas
            m2totconv+=m2prod
            m2totconvwaste+=m2prodmala

    #Ahora saco el dato de corrugado ***Acá saco sólo las GoodQTY, porque el waste que declara la fosber es el que sale durante el wetend? y no en el stacker??? No se le imprime tarja??

    cursor.execute("SELECT TOP (3000)[SETUPID],[BOARDWIDTH],[GRADEID],[UKORDERID],[UKBLANKWIDTH],[UKBLANKLENGTH],[UKTOTALQTY],[UKGOODQTY],[UKPLANNEDQTY],[UKPLANNEDTOTAL],[UKNUMBERACROSS],[UKCOMPLETEFLAG],[LKORDERID],[LKBLANKWIDTH],[LKBLANKLENGTH],[LKTOTALQTY],[LKGOODQTY],[LKPLANNEDQTY],[LKPLANNEDTOTAL],[ACTUALSTARTDATE],[ACTUALENDDATE],[LINER1],[MEDIUM1],[LINER2],[MEDIUM2],[LINER3],[MEDIUM3],[LINER4],[LINER1WIDTH],[MEDIUM1WIDTH],[LINER2WIDTH],[MEDIUM2WIDTH],[LINER3WIDTH],[MEDIUM3WIDTH],[LINER4WIDTH],[ROWID],[TOTALLINEAL],[GOODLINEAL],[WASTELINEAL] FROM [ctidb_transact].[dbo].[CORRUGATORPROD]  where ACTUALSTARTDATE Between '"+ ini +"' And '"+ fin +"' order by transactionindex desc")

    resultado=[]
    m2totcorr=0
    m2totcorrwaste=0
    #print("datos obtenidos entre " + ini + " y " + fin + ":")
    for row in cursor.fetchall():
        #print(row)

        m2placaUK=row[4]*row[5]
        unidsUK=row[6]
        m2prodUK=m2placaUK*unidsUK

        m2placaLK=row[13]*row[14]
        unidsLK=row[15]
        m2prodLK=m2placaLK*unidsLK

        m2totcorr += m2prodLK + m2prodUK
        #print("Suma m2 row: " + str(m2prodLK) + " " + str(m2prodUK))

    resultado=[m2totconv,m2totcorr,m2totconvwaste,m2totcorrwaste]
    #print("Suma total segmento Corr: "+ ini+ " - "+ fin + " "+ str(m2totcorr))
    #sleep(5)
    return(resultado)


'''
print("iniciando")
print(consulta(datetime.now()-timedelta(days=3),datetime.now() ))
print("fin")
'''

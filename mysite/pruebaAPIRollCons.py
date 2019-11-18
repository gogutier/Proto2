import requests
import zeep
from datetime import datetime, timedelta

import xmltodict


def cargaconsbob( fechaini, fechafin):

    wsdl = 'http://192.168.8.42/CTIRollstockWebService/ServiceRollStockManagement.svc?wsdl'
    client = zeep.Client(wsdl=wsdl)
    #data=(client.service.GetRollStock())

    A= fechaini.strftime("%m-%d-%Y %H:%M")
    B= fechafin.strftime("%m-%d-%Y %H:%M")
    print(A)
    print(B)
    AA ='03-03-2019 07:00'
    BB = '05-03-2019 07:00'
    data=(client.service.GetRollConsumptionDetails('<CTI><RollStorage><Plant><ID>800</ID></Plant></RollStorage></CTI>', A, B) )#('800',A,B))



    doc = xmltodict.parse(data)
    #print(doc)
    #print(len(doc['CTI']['RollConsumption']))

    lista=[]

    #acá falta el caso en que no encuentre nada
    try:
        for i in range(0,len(doc['CTI']['RollConsumption'])):

            RollID=doc['CTI']['RollConsumption'][i]['RollID']
            RollStandID=doc['CTI']['RollConsumption'][i]['RollStandID']
            formato=doc['CTI']['RollConsumption'][i]['Width']['#text']
            peso=doc['CTI']['RollConsumption'][i]['Weight']['#text']
            grado=doc['CTI']['RollConsumption'][i]['PaperGradeID']
            diametro=doc['CTI']['RollConsumption'][i]['Diameter']['#text']
            mlusados=doc['CTI']['RollConsumption'][i]['LinealUsed']['#text']
            mlrestantes=doc['CTI']['RollConsumption'][i]['LinealLeft']['#text']
            peelwaste=doc['CTI']['RollConsumption'][i]['PeelWasteLineal']['#text']


            #print(doc['CTI']['RollConsumption'][3]['ActualWidth']['@UOM'])
            #print(doc['CTI']['RollConsumption'][i]['LinealUsed']['#text'])
            #print(doc['CTI']['RollConsumption'][i]['LinealLeft']['#text'])
            #print(doc['CTI']['RollConsumption'][i]['Diameter']['#text'])
            #print(doc['CTI']['RollConsumption'][i]['PeelWasteLineal']['#text'])
            #print(doc['CTI']['RollConsumption'][3]['RollStatus'])
            #print(doc['CTI']['RollConsumption'][3]['RollStorageDetails']['Plant']['Warehouse']['ID'])
            #print(doc['CTI']['RollConsumption'][3]['RollStorageDetails']['Plant']['Warehouse']['Location']['ID'])
            rollo={'RollID':RollID,'RollStandID':RollStandID, 'formato':formato, 'peso':peso , 'grado':grado, 'diametro':diametro, 'mlusados':mlusados, 'mlrestantes':mlrestantes,'peelwaste':peelwaste}
            #print(doc['CTI']['Roll'][i]['ID'])

            lista.append(rollo)
    except:
        print("no se encontró consumo de rollos en ese turno")
    return(lista)

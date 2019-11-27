import requests
import zeep
from datetime import datetime, timedelta

import xmltodict


def cargaconsbob(fechaini, fechafin):

    wsdl = 'http://192.168.8.42/CTIRollstockWebService/ServiceRollStockManagement.svc?wsdl'
    client = zeep.Client(wsdl=wsdl)
    #data=(client.service.GetRollStock())

    A= fechaini.strftime("%m-%d-%Y %H:%M")
    B= fechafin.strftime("%m-%d-%Y %H:%M")
    #print(A)
    #print(B)
    AA ='11-18-2019 14:30'
    BB ='11-18-2019 22:30'
    data=(client.service.GetRollConsumptionDetails('<CTI><RollStorage><Plant><ID>800</ID></Plant></RollStorage></CTI>', A, B) )#('800',A,B))


    #print(data)
    doc = xmltodict.parse(data, process_namespaces=True)
    #print(doc['CTI'])
    #print(len(doc['CTI']['RollConsumption']))
    #(doc['CTI']['RollConsumption'])

    lista=[]
    flag1consumo=0

    #acá falta el caso en que no encuentre nada
    try:
        print("************* Imprimiendo cada dict asociado a un consumo: *****************")
        #print(len(doc['CTI']))
        try:
            aux=(doc['CTI']['RollConsumption']['RollID'])
            print("Flag será 1, significa que sólo hay una bobina consumida en ese rango de fecha")
            flag1consumo=1
        except:
            flag1consumo=0
            #print(doc['CTI']['RollConsumption'])
            print("Flag será 0")


        if flag1consumo==0:
            for i in doc['CTI']['RollConsumption']:#range(0,len(doc['CTI']['RollConsumption'])-1 ):
                #print(i['RollID'])

                RollID=i['RollID']
                RollStandID=i['RollStandID']
                formato=i['Width']['#text']
                peso=i['Weight']['#text']
                grado=i['PaperGradeID']
                diametro=i['Diameter']['#text']
                mlusados=i['LinealUsed']['#text']
                mlrestantes=i['LinealLeft']['#text']
                peelwaste=i['PeelWasteLineal']['#text']

                rollo={'RollID':RollID,'RollStandID':RollStandID, 'formato':formato, 'peso':peso , 'grado':grado, 'diametro':diametro, 'mlusados':mlusados, 'mlrestantes':mlrestantes,'peelwaste':peelwaste}
                #print(doc['CTI']['Roll'][i]['ID'])
                print("rollo: ")
                print(rollo)
                lista.append(rollo)

        elif flag1consumo==1:
            #print(doc['CTI']['RollConsumption']['RollID'])
            RollID=doc['CTI']['RollConsumption']['RollID']
            RollStandID=doc['CTI']['RollConsumption']['RollStandID']
            formato=doc['CTI']['RollConsumption']['Width']['#text']
            peso=doc['CTI']['RollConsumption']['Weight']['#text']
            grado=doc['CTI']['RollConsumption']['PaperGradeID']
            diametro=doc['CTI']['RollConsumption']['Diameter']['#text']
            mlusados=doc['CTI']['RollConsumption']['LinealUsed']['#text']
            mlrestantes=doc['CTI']['RollConsumption']['LinealLeft']['#text']
            peelwaste=doc['CTI']['RollConsumption']['PeelWasteLineal']['#text']


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
            print("rollo: ")
            print(rollo)
            lista.append(rollo)

        #print(lista)
    except Exception as e:
        print(e)
        print("no se encontró consumo de rollos en ese turno")
    return(lista)

#cargaconsbob(datetime.now(), datetime.now())

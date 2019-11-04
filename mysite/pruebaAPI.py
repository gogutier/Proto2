import requests
import zeep

import xmltodict




wsdl = 'http://192.168.8.42/CTIRollstockWebService/ServiceRollStockManagement.svc?wsdl'
client = zeep.Client(wsdl=wsdl)
data=(client.service.GetRollStock())


print(data)

doc = xmltodict.parse(data)

#print (doc)
print(len(doc['CTI']['Roll']))
#for i in range(0,len(doc['CTI']['Roll'])):
'''
    print(doc['CTI']['Roll'][3]['ID'])
    print(doc['CTI']['Roll'][3]['PaperGradeID'])
    print(doc['CTI']['Roll'][3]['ActualWidth']['@UOM'])
    print(doc['CTI']['Roll'][3]['ActualWidth']['#text'])
    print(doc['CTI']['Roll'][3]['Lineal']['#text'])
    print(doc['CTI']['Roll'][3]['RollStatus'])
    print(doc['CTI']['Roll'][3]['RollStorageDetails']['Plant']['Warehouse']['ID'])
    print(doc['CTI']['Roll'][3]['RollStorageDetails']['Plant']['Warehouse']['Location']['ID'])
'''
    #print(doc['CTI']['Roll'][i]['ID'])
#print(doc['PA-185830']['Status'])

data=(client.service.GetRollSummary(456181))


print(data)

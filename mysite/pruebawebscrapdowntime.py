from __future__ import print_function
import mechanicalsoup
import argparse
from getpass import getpass

from datetime import datetime, timedelta
from time import time, sleep

#parser = argparse.ArgumentParser(description="Interlink.")
#parser.add_argument("username")
#args = parser.parse_args()

#args.password = getpass("Please enter your Interlink password: ")

def webscrap_wip(maq, fini, ffin):


    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='MyBot/0.1: mysite.example.com/bot_info',
    )
    # Uncomment for a more verbose output:
    # browser.set_verbose(2)

    browser.open("http://interlink.corrupac.cl/pagegenerator.dll/Login")
    #browser.follow_link("login")
    browser.select_form()
    #browser.select_form('formMain')
    browser["User"] = "plant"#args.username
    browser["password"] = "plant"#args.password
    resp = browser.submit_selected()

    # Uncomment to launch a web browser on the current page:
    #browser.launch_browser()

    #print(browser.open("http://interlink.corrupac.cl"))

    #>>> browser.follow_link("forms") #sigue el link que tenga la palabra indicada
    #<Response [200]>
    #>>> browser.get_url()

    # verify we are now logged in
    page = browser.get_current_page()
    #print(page)
    messages = page.find_all(id="SIMPLETRANSCAR")
    #print(messages)
    link = browser.find_link(id="SIMPLETRANSCAR")
    #assert page.select(".logout-form")

    browser.follow_link(link)


    print(page.title.text)
    #print(browser.get_current_page())

    #Falta hacer que selecciones la opción 800 en plant y luego apriete la el form submit, esto en el explorador al parecer lo hace solo (script?)

    #Acá es donde tengo que ingresar lo parámetros: Máquina a consultar y Rango de fechas.
    maquina=str(maq)
    fechaini=fini.strftime("%Y-%m-%d+%H:%M")
    fechafin=ffin.strftime("%Y-%m-%d+%H:%M")
    browser.open("http://interlink.corrupac.cl/pagegenerator.dll/ExtendedDowntime?StationLink="+maquina+"&StartDate="+fechaini+"&EndDate="+fechafin)
    #browser.open("http://interlink.corrupac.cl/pagegenerator.dll/ExtendedRWU?dateFrom=2019-08-01+00%3A00&dateTo=2019-8-16+23%3A59")


    #browser.open("http://interlink.corrupac.cl/pagegenerator.dll/ExtendedTransCar?MachineLink=0&PlantLink=1")
    #browser.open("http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID")
    #browser.launch_browser()



    page= browser.get_current_page()

    table = page.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="dataTable")
    #rows = table.findAll(lambda tag: tag.name=='tbody')
    rows = table.findAll(lambda tag: tag.name=='tr')# and tag.has_attr('class') and tag['class']=="C60")
    tabla=[]
    tabla2=[]
    for row in rows[1:]:
        fila=[]
        cols = row.findAll(lambda tag: tag.name=='td')
        '''
        #if 'bgcolor' in tr.attrs and tr.attrs['bgcolor']=='#CEE3F6':
        if 'bgcolor' in row.attrs:# and tr.attrs['bgcolor']=='#CEE3F6':
            #print(row.attrs['bgcolor'])
            fila.append(row.attrs['bgcolor'])
        else:
            fila.append("#0")
        '''

        for col in cols:
            #print(col.text)
            fila.append(col.text)

        tabla.append(fila)
    #print(tabla)

    #ahora borro las filas que sean del tipio Scheduled:
    for fila in tabla:

        if fila[4]=="Scheduled":
          tabla.remove(fila)



    return(tabla)

'''
fechaini=datetime.strptime("02-03-2020 07:00:00", "%d-%m-%Y %H:%M:%S")
fechafin=datetime.strptime("02-04-2020 07:00:00", "%d-%m-%Y %H:%M:%S")
maq=4
for fila in webscrap_wip(maq,fechaini,fechafin):
    print(fila)
'''

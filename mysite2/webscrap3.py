from __future__ import print_function
import mechanicalsoup
import argparse
from getpass import getpass

from time import time, sleep
#parser = argparse.ArgumentParser(description="Interlink.")
#parser.add_argument("username")
#args = parser.parse_args()

#args.password = getpass("Please enter your Interlink password: ")

def webscrap_prog_corr():


    browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='MyBot/0.1: mysite.example.com/bot_info',
    )
    # Uncomment for a more verbose output:
    # browser.set_verbose(2)
    flag=0
    try:
        browser.open("http://192.168.8.42/pagegenerator.dll/Login")
    except:
        browser.open("http://interlink.corrupac.cl/pagegenerator.dll/Login")
        flag=1
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

    if flag==0:
        browser.open("http://192.168.8.42/pagegenerator.dll/CorrugatorLineupDryend?AreaLink=1")
    else:
        browser.open("http://interlink.corrupac.cl/pagegenerator.dll/CorrugatorLineupDryend?AreaLink=1")
    #browser.open("http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID")
    #browser.launch_browser()
    #print(browser.get_current_page())

    page = browser.get_current_page()
    #print(page)

    #rows=[el.text for el in page.find_all(['td', 'th']) if el.text]

    table = page.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="dataTable")
    rows = table.findAll(lambda tag: tag.name=='tbody')
    rows = table.findAll(lambda tag: tag.name=='tr')# and tag.has_attr('class') and tag['class']=="C60")
    tabla=[]
    tabla2=[]
    for row in rows:

        fila=[]
        cols = row.findAll(lambda tag: tag.name=='td')

        #if 'bgcolor' in tr.attrs and tr.attrs['bgcolor']=='#CEE3F6':
        if 'bgcolor' in row.attrs:# and tr.attrs['bgcolor']=='#CEE3F6':
            #print(row.attrs['bgcolor'])
            fila.append(row.attrs['bgcolor'])
        else:
            fila.append("#0")

        for col in cols:
            #print(col.text)
            fila.append(col.text)

        tabla.append(fila)
    #print(tabla)

    #ahora borro las filas que no tengan 7 columnas:
    #for fila in tabla:
    #    if len(fila)<5:
    #        tabla.remove(fila)

    for i in range(2,len(tabla)):
        col=[]

        col.append(tabla[i][0][1:])
        col.append(tabla[i][2][1:])
        col.append(tabla[i][3])
        col.append(tabla[i][4])
        col.append(tabla[i][5])
        col.append(tabla[i][6])
        col.append(tabla[i][7])
        col.append(tabla[i][8])
        col.append(tabla[i][11])
        col.append(tabla[i][12])
        col.append(tabla[i][13])
        col.append(tabla[i][28])
        col.append(tabla[i][31])
        col.append(tabla[i][32])
        col.append(tabla[i][33])



        tabla2.append(col)





    #[el.text for el in sp.find_all(['td', 'th']) if el.text]
    #print(tabla2)
    #sleep(30)

    return(tabla2)

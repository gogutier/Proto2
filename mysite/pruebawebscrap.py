from __future__ import print_function
import mechanicalsoup
import argparse
from getpass import getpass

#parser = argparse.ArgumentParser(description="Interlink.")
#parser.add_argument("username")
#args = parser.parse_args()

#args.password = getpass("Please enter your Interlink password: ")

def webscrap_wip():


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


    browser.open("http://interlink.corrupac.cl/pagegenerator.dll/ExtendedTransCar?MachineLink=0&PlantLink=1")
    #browser.open("http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID")
    #browser.launch_browser()
    #print(browser.get_current_page())



    #print(page)
    pagetxt  = browser.get_current_page().text
    #print("ini")
    numinicio = browser.get_current_page().text.find("PiecesAvail1 = new Array")#.text
    #print(numinicio)
    numfin=pagetxt[numinicio+24:numinicio+6000].find("'z'")-2
    #print(numfin)
    datatxt=pagetxt[numinicio+24:numinicio+numfin+24]
    #print(datatxt)

    lista=datatxt.split("],[")

    #print(len(lista))
    for i in range(0,len(lista)):
        lista[i]=lista[i].replace('parseInt(','')
        lista[i]=lista[i].replace(')','')
        lista[i]=lista[i].replace('(','')
        lista[i]=lista[i].replace('[','')
        lista[i]=lista[i].replace(']','')
        lista[i]=lista[i].split(",")
        for j in range(0,len(lista[i])):
            lista[i][j]=float(lista[i][j])
            #print(lista[i][j])
        #print(lista[i])
        #print(lista[i][1])

    ## N° máquina, n° piezas, Area, n° órdenes


    #print("Mostrando resumen por máquina")

    #print("Maqunina 2:")
    #(maq, num maq)
    maqs = [("FFG",2), ("TCY",4), ("FFW",27), ("DRO",5) , ("WRD",12) , ("HCR",11), ("DIM",13), ("CORR",0)]


    corrarea=browser.get_current_page().find_all(class_="rpad")[9].text
    corrpiezas=browser.get_current_page().find_all(class_="rpad")[9].text
    corrarea=float(corrarea[corrarea.find("(")+1:corrarea.find(")")])
    corrpiezas=float(corrpiezas[0:corrpiezas.find(" ")].replace(",","."))
    #print(corrpiezas)

    #prin(browser.get_current_page().find("a", class_="u-linkComplex").text)


    resultado=[]
    for maquina in maqs:
        #se suma el área sólo si el número de piezas es positivo
        auxsumarea=0
        auxsumapiezas=0
        for list in lista:

            if list[0]==maquina[1]:
                if list[1]>0:
                    auxsumarea=auxsumarea+list[2]
                    auxsumapiezas=auxsumapiezas+list[1]

 

        #print(maquina[0] + ": " + str(auxsumarea) + ", " + str(auxsumapiezas))
        if maquina[0]=="CORR":
            resultado.append([maquina[0],corrpiezas, corrarea])
        else:
            resultado.append([maquina[0],auxsumapiezas, auxsumarea])

    return(resultado)

print(webscrap_wip())

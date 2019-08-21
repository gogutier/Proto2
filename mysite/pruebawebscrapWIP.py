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

    browser.open("http://interlink.corrupac.cl/pagegenerator.dll/ExtendedRWU?dateFrom=2019-08-01+00%3A00&dateTo=2019-8-16+23%3A59")
    #browser.open("http://interlink.corrupac.cl/pagegenerator.dll/ExtendedTransCar?MachineLink=0&PlantLink=1")
    #browser.open("http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID")
    browser.launch_browser()



    print(browser.get_current_page().text)
    pagetxt  = browser.get_current_page().text

        #print(lista[i])
        #print(lista[i][1])

    ## N° máquina, n° piezas, Area, n° órdenes


    #print("Mostrando resumen por máquina")

    #print("Maqunina 2:")
    #(maq, num maq)
    maqs = [("FFG",2), ("TCY",4), ("FFW",27), ("DRO",5) , ("WRD",12) , ("HCR",11)]#, ("DIM",13)]


    resultado=[]


    return(resultado)

print(webscrap_wip())

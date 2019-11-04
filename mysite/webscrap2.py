#from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.firefox.options import Options

from time import time, sleep



def webscrap_corrplan():
    #options = Options()
    #options.add_argument("--headless")
    corrplan=[]
    if 1:#with Display(visible=True):
        # we can now start Firefox and it will run inside the virtual display
        #binary = FirefoxBinary('/home/gonzalo/Descargas/firefox-17.0.1/firefox/firefox-bin')#esto hay que cambiarlo al exportarlo a pythonanywhere, pasarlo a : "driver = webdriver.Firefox()""
        #driver = webdriver.Firefox(firefox_options=options, executable_path="C:\\Utility\\BrowserDrivers\\geckodriver.exe")
        #binary = FirefoxBinary('/home/gonzalo/Descargas/firefox-17.0.1/firefox/firefox-bin')
        #driver = webdriver.Firefox(firefox_binary=binary)
        driver = webdriver.Chrome(executable_path='chromedriver.exe')#, options=options)

        # put the rest of our selenium code in a try/finally
        # to make sure we always clean up at the end

        direccion= "http://192.168.8.42//pagegenerator.dll/Login"
        direccion2= "http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID&wait="
        auxdir=0
        try:
            #browser.get('http://www.google.com')
            #driver.get("http://interlink.corrupac.cl/pagegenerator.dll/Login")

            print("entrando a login")

            try:
                driver.get(direccion)
            except:
                auxdir=1
                driver.get(direccion2)


            driver.implicitly_wait(30)
            print (driver.title) #this should print "Google"
            driver.implicitly_wait(30)
            #elem = driver.find_element_by_id("email")
            #elem.send_keys(user)

            #print(driver.page_source)
            print("ingresando user y pass")
            search_field = driver.find_element_by_id("LoginPh")
            search_field.clear()
            search_field.send_keys("Plant")

            search_field = driver.find_element_by_id("PasswordPh")
            print(search_field)
            search_field.clear()
            search_field.send_keys("plant")

            sleep(5)
            search_field = driver.find_element_by_id("btnlogin")
            print(search_field)
            search_field.click()
            #driver.find_element_by_name("submit").submit()
            #driver.implicitly_wait(20)

            print("entrando a la lista de ordenes corrplan")
            """
            lists= driver.find_elements_by_id("SIMPLECPORDERS")
            for listitem in lists:
                print (listitem.get_attribute("innerHTML"))
            sleep(5)
            link = driver.find_element_by_link_text('Reporte de Ordenes de CorrPlan')
            link.click()
            driver.implicitly_wait(20)
            #print(driver.page_source)
            """
            #driver.get("http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID&wait=")
            if auxdir==0:
                driver.get("http://192.168.8.42/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID&wait=")
            else:
                driver.get("http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID&wait=")
            #
            try:
                myElem = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'dataTable_info')))
                print ("Page is ready!")
            except TimeoutException:
                print ("Loading took too much time!")
            '''
            i=0
            lists= driver.find_elements_by_class_name("even")#tambièn hay de clase even
            for listitem in lists:
                print (listitem.get_attribute("innerHTML"))
                i=i+1
            print("total elementos: " + str(i))
            '''

            '''
            lists= driver.find_elements_by_role_name("row")
            for listitem in lists:
                print (listitem.get_attribute("innerHTML"))
            '''

            table = driver.find_element_by_id('dataTable')

            head = table.find_element_by_tag_name('thead')
            body = table.find_element_by_tag_name('tbody')


            body_rows = body.find_elements_by_tag_name('tr')
            i=0

            print("analizando tabla")
            for row in body_rows:

                i=i+1
                print("analizando row " + str(i) )
                data = row.find_elements_by_tag_name('td')
                file_row = []
                for datum in data:
                    #print("analizando data")
                    datum_text = datum.text#.encode('utf8')
                    file_row.append(datum_text)
                corrplan.append(file_row)

            print(corrplan)
            print("Total filas: " + str(i))



            #print(driver.page_source)

        finally:
            driver.quit()
        return(corrplan)

#print(webscrap_corrplan())
#########################3

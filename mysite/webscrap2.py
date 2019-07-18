from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary




def webscrap_corrplan():
    corrplan=[]
    with Display():
        # we can now start Firefox and it will run inside the virtual display
        binary = FirefoxBinary('/home/gonzalo/Descargas/firefox-17.0.1/firefox/firefox-bin')#esto hay que cambiarlo al exportarlo a pythonanywhere, pasarlo a : "browser = webdriver.Firefox()""
        #binary = FirefoxBinary('/home/gonzalo/Descargas/firefox-17.0.1/firefox/firefox-bin')
        driver = webdriver.Firefox(firefox_binary=binary)

        # put the rest of our selenium code in a try/finally
        # to make sure we always clean up at the end
        try:
            #browser.get('http://www.google.com')
            driver.get("http://interlink.corrupac.cl/pagegenerator.dll/Login")
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
            search_field.clear()
            search_field.send_keys("plant")


            search_field = driver.find_element_by_id("btnlogin")
            search_field.submit()
            driver.implicitly_wait(20)

            lists= driver.find_elements_by_id("SIMPLECPORDERS")
            for listitem in lists:
                print (listitem.get_attribute("innerHTML"))

            link = driver.find_element_by_link_text('Reporte de Ordenes de CorrPlan')
            link.click()
            driver.implicitly_wait(20)
            #print(driver.page_source)
            driver.get("http://interlink.corrupac.cl/pagegenerator.dll/OrderStatusCorrplan?%21+link=OpMachineLink+in%282%2C+4%2C+27%2C+5%2C+12%2C+11%29%29&order+by=DueDateTime%2COrderID&wait=")
            driver.implicitly_wait(30)

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
            for row in body_rows:
                i=i+1
                data = row.find_elements_by_tag_name('td')
                file_row = []
                for datum in data:
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

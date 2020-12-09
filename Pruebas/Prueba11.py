import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.chrome.options import Options
#### pruebas de ingresar 
class usando_unitest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
#Ingresar contrato
    def test_Ingresar_contrato(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("admin")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("admin")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        # ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a crear contrato
        driver.find_element_by_xpath("/html/body/main/section/div/div/div[4]/div/div[2]/input").click()
        time.sleep(1)
        #seleccionar fecha
        datefield = driver.find_element_by_name('fecha_termino')
        datefield.click()
        datefield.send_keys("15012021")
        #seleccionar cliente por rut en el codigo
        SeleccionarC = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/p[3]/select"))
        SeleccionarC.select_by_value("19792703-9")
        #seleccionar profesional por rut en el codigo
        SeleccionarP = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/p[4]/select"))
        SeleccionarP.select_by_value("19792703-8")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/center/button").click()
        time.sleep(4)
        if driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[1]").text=='Contrato: agregado':
            print("Se a ingresado el contrato con exito")
        else:
            print("no se ingreso el contrato")

    def cerrar5(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
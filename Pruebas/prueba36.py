import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.chrome.options import Options
class usando_unitest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
#ver Crear Checklist
    def test_crear_Checklist(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Profesional")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        #ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a crear Check
        driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[3]/div/div[2]/input").click()
        time.sleep(1)
        descrip = driver.find_element_by_name("descripcion_check")
        descrip.send_keys("Prueba1")
        ####################### luego cambiar a 19792703-9
        Seleccionar = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/div/p[2]/select"))
        Seleccionar.select_by_value("19792703-9")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/center/button").click()
        time.sleep(1)
        ############# Seleccionar condicion
        SeleccionarC1 = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/p[3]/select"))
        SeleccionarC1.select_by_value("1")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/p[3]/button").click()
        time.sleep(2)
        SeleccionarC2 = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/p[3]/select"))
        SeleccionarC2.select_by_value("3")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/p[3]/button").click()
        time.sleep(2)
        SeleccionarC3 = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/p[3]/select"))
        SeleccionarC3.select_by_value("13")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/p[3]/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/div[2]/center/a[1]").click()
        time.sleep(1)
        if driver.current_url=='http://127.0.0.1:8000/listadoChecklist.html':
            print("Se a agregado un nuevo Checklist ")
        else:
            print("Error no se agrego Checklist")

    def cerrar15(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
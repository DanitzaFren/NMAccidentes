import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#ver eliminar profesional
    def test_eliminar_profesional(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Benja")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        #ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a ver listdo de profesionales
        driver.find_element_by_xpath("/html/body/main/section/div/div/div[1]/div/div[3]/input").click()
        time.sleep(2)
        #seleccionar eliminar
        alert = Alert(driver)
        driver.find_element_by_xpath("/html/body/main/section[2]/div/center/div[1]/table/tbody/tr[1]/td[5]/a[2]").click()
        alert.accept()
        if driver.title=='Listado Profesionales':
            print("Se elimino el profesional ")
        else:
            print("No permite eliminar profesional")

    def cerrar1(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
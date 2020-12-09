import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#Ver modificar condicion
    def test_modificar_condicion(self):
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
        # ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a ver listdos de las  condiciones
        driver.find_element_by_xpath("/html/body/main/section/div/div/div[3]/div/div[3]/input").click()
        #seleccionar la ultima condicion agregada
        driver.find_element_by_xpath("/html/body/main/section[2]/div/center/div[1]/table/tbody/tr[15]/td[3]/a[1]").click()
        condicion = driver.find_element_by_name("nom_condicion")
        condicion.send_keys("prueba2")
        time.sleep(2)
        alert = Alert(driver)
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/button").click()
        alert.accept()
        if driver.current_url=='http://127.0.0.1:8000/listadoCondicion.html':
            print("Se modifico la condicion")
        else:
            print("no permite que se modifique la condicion")

    def cerrar7(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
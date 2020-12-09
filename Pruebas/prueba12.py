import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
# ver modifica a un profesional
    def test_modificar_profesional(self):
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
        #selecciona a un profesional para modificar
        driver.find_element_by_xpath("/html/body/main/section[2]/div/center/div[1]/table/tbody/tr[1]/td[5]/a[1]").click()
        time.sleep(2)
        nombre = driver.find_element_by_id("id_nombre")
        #clear limpia el campo
        nombre.clear()
        nombre.send_keys("Prueba1")
        materno = driver.find_element_by_id("id_materno")
        materno.clear()
        materno.send_keys("Prueba2")
        time.sleep(2)
        alert = Alert(driver)
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/center/button").click()
        alert.accept()
        if driver.current_url=='http://127.0.0.1:8000/listadoProfesionales_N.html':
            print("El profesional se modifico correctamente ")
        else:
            print("no se modificar el profesional")

    def cerrar1(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
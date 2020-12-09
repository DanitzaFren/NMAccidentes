import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#reportar accidente cliente 
    def test_reportar_accidente_cliente(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Cliente")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        # ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a ver reportar Accidente
        driver.find_element_by_xpath("/html/body/main/section/div/section[1]/div/div/div[3]/div/div[2]/input").click()
        time.sleep(2)
        Descripcion = driver.find_element_by_name("descripcion")
        Descripcion.send_keys("Prueba1")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[2]/form/center/button").click()
        alert = Alert(driver)
        alert.accept()
        time.sleep(2)
        #valida el mensaje del sistema
        if driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[1]").text=='Accidente: Reporte enviado':
            print("Se reporto un accidente ")
        else:
            print("no Se reporto un accidente ")


    def cerrar1(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#rver solicitar_Servicios_Visita
    def test_solicitar_Servicios_Visita_cliente(self):
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
        #ir a Solicitar servicio
        driver.find_element_by_xpath("/html/body/main/section/div/section[1]/div/div/div[1]/div/div[2]/input").click()
        time.sleep(2)
        # seleccionar en un select
        Seleccionar = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[2]/form/p[3]/select"))
        Seleccionar.select_by_value("3")
        Descr = driver.find_element_by_name("descripcion")
        Descr.send_keys("Prueba4")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[2]/form/center/button").click()
        if driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[1]").text=='Solicitud: agregado':
            print("Se solicito una nueva Visita  ")
        else:
            print("no solicito Visita ")

    def cerrar5(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
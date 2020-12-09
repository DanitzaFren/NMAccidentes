import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#ver Crear asesoria
    def test_crear_asesoria(self):
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
        driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[2]/div/div[2]/input").click()
        time.sleep(1)
        #selec fecha
        datefield = driver.find_element_by_name('fecha')
        datefield.click()
        datefield.send_keys("21012021")
        ####################### luego cambiar a 1
        Seleccionar = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[2]/form/div/p[2]/select"))
        Seleccionar.select_by_value("21")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[2]/form/center/button").click()
        if driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div[1]").text=='Asesoría: Asesoria Creada':
            print("Se a agregado un nueva asesoria ")
        else:
            print("Error no se agrego asesoria")

    def cerrar17(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
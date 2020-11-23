import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
# Inicio de ingresar Profesional
    def test_iniciar_sesion_profesional(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("admin")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//html/body/header/div/nav/ul/li[4]/a").click()
        driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[1]/div/div[2]/input").click()
        time.sleep(6)
        self.assertIn("Ingresar Profesional", driver.title)
        usuario = driver.find_element_by_id("id_rut_profesional")
        usuario.send_keys("19792704")
        id_dv = driver.find_element_by_id("id_dv")
        id_dv.send_keys("8")
        nombre = driver.find_element_by_id("id_nombre")
        nombre.send_keys("Heather")
        paterno = driver.find_element_by_id("id_paterno")
        paterno.send_keys("Mason")
        materno = driver.find_element_by_id("id_materno")
        materno.send_keys("Hola1")
        materno = driver.find_element_by_id("id_contrasena")
        materno.send_keys("duoc123456")
        estado = driver.find_element_by_id("id_estado")
        estado.send_keys("Activo")
        select = Select(driver.find_element_by_id('id_id_admin'))
        select.select_by_value('1')
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/center/button").click()
        time.sleep(6)

    def cerrar(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()

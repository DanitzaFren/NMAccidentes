import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

#### pruebas de ingresar 
class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
# Inicio de crear Profesional
    def test_Crear_profesional(self):
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
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/main/section/div/div/div[1]/div/div[2]/input").click()
        time.sleep(2)
        self.assertIn("Ingresar Profesional", driver.title)
        rut = driver.find_element_by_id("txtRut")
        rut.send_keys("197927038")
        nombre = driver.find_element_by_id("id_nombre")
        nombre.send_keys("Benjamin")
        paterno = driver.find_element_by_id("id_paterno")
        paterno.send_keys("Bravo")
        materno = driver.find_element_by_id("id_materno")
        materno.send_keys("Diaz")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/center/button").click()
        time.sleep(2)
        username = driver.find_element_by_id("id_username")
        username.send_keys("Profesional")
        contraa = driver.find_element_by_id("id_password1")
        contraa.send_keys("duoc123456")
        contras = driver.find_element_by_id("id_password2")
        contras.send_keys("duoc123456")
        email = driver.find_element_by_id("id_email")
        email.send_keys("prueba@gmail.com")
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/center/button").click()
        time.sleep(2)
        if driver.current_url=='http://127.0.0.1:8000/servicios':
            print("Se a creado el profesional con exito ")
        else:
            print("no se pudo ingresar el profesional")

    def cerrar(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
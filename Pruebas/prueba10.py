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
# valida el formulario del cliente
    def test_valida_formulario_cliente(self):
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
        driver.find_element_by_xpath("/html/body/main/section/div/div/div[2]/div/div[2]/input").click()
        time.sleep(2)
        self.assertIn("Ingresar Cliente", driver.title)
        rut = driver.find_element_by_name("id_cliente")
        rut.send_keys("197927038")
        nombre = driver.find_element_by_name("nombre")
        nombre.send_keys("Contru. pro")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/center/button").click()
        time.sleep(2)
        if driver.current_url=='http://127.0.0.1:8000/crearCliente.html':
            print("Se a validado los campos del formulario")
        else:
            print("Error en validacion del formulario cliente")

    def cerrar4(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
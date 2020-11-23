import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
# Inicio de sesion del Administrador
    def test_iniciar_sesion_admin(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("admin")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "No se encontro el elemento:" not in driver.page_source
        if driver.current_url=='http://127.0.0.1:8000/':
            print("Login del administrador correcto ")
        else:
            print("Error en la pagina")

    def tearDown(self):
        self.driver.close()

# Inicio de sesion del profesional
    def test_iniciar_sesion_profesional(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Profesional")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "No se encontro el elemento:" not in driver.page_source
        if driver.current_url=='http://127.0.0.1:8000/':
            print("Login del profesional correcto")
        else:
            print("Error en la pagina")

    def cerrar(self):
        self.driver.close()
        
# Inicio de sesion del Cliente
    def test_iniciar_sesion_Cliente(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Cliente")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "No se encontro el elemento:" not in driver.page_source
        if driver.current_url=='http://127.0.0.1:8000/':
            print("Login del cliente correcto")
        else:
            print("Error en la pagina")

    def cerrar1(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


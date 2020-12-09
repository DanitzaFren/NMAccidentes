import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#### pruebas de logins
class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
# Inicio de sesion del Administrador
    def test_iniciar_sesion_admin(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("admin")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("admin")
        usuario.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "No se encontro el elemento:" not in driver.page_source
        if driver.current_url=='http://127.0.0.1:8000/':
            print("Login del administrador correcto ")
        else:
            print("Login del administrador incorrecto")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

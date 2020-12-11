import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#### pruebas de logins
class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
# ingresar con numeros en el usuario
    def test_iniciar_con_numeros(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("admin12345")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("")
        usuario.send_keys(Keys.ENTER)
        time.sleep(2)
        assert "No se encontro el elemento:" not in driver.page_source
        if driver.current_url=='http://127.0.0.1:8000/accounts/login/':
            print("Validador de usuario correcto ")
        else:
            print("Validador de usuario no funcionando")

    def tearDown1(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
import warnings


#### pruebas de logins
class usando_unitest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
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
        time.sleep(5)
        assert "No se encontro el elemento:" not in driver.page_source
        if driver.current_url=='http://127.0.0.1:8000/':
            print("Login del administrador correcto ")
        else:
            print("Login del administrador incorrecto")

    def tearDown(self):
        self.driver.close()
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
if __name__ == "__main__":
    unittest.main()


   
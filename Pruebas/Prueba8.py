import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.chrome.options import Options
#### pruebas de ingresar 
class usando_unitest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
# ver listado de profesionales
    def test_ver_listado_Profesionales(self):
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
        #ir a servicios
        driver.get("http://127.0.0.1:8000/servicios.html")
        time.sleep(2)
        #ir a ver listdo de profesionales
        driver.get("http://127.0.0.1:8000/listadoProfesionales_N.html")
        time.sleep(2)
        if driver.current_url=='http://127.0.0.1:8000/listadoProfesionales_N.html':
            print("Ver listado de los profesionales.")
        else:
            print("no muestra los profesionales")

    def cerrar1(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
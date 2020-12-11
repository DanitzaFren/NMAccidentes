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
# valida el formulario del cliente
    def test_valida_formulario_cliente(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("admin")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("admin")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/servicios.html")
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/crearCliente.html")
        time.sleep(2)
        self.assertIn("Ingresar Cliente", driver.title)
        rut = driver.find_element_by_name("id_cliente")
        rut.send_keys("197927038")
        nombre = driver.find_element_by_name("nombre")
        nombre.send_keys("Contru. pro")
        time.sleep(2)
        nombre.send_keys(Keys.ENTER)
        time.sleep(2)
        if driver.current_url=='http://127.0.0.1:8000/crearCliente.html':
            print("Se ha validado los campos del formulario, no se puede dejar campos en blanco o ingresar tipos de datos incorrectos.")
        else:
            print("Error en validacion del formulario cliente")

    def cerrar4(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
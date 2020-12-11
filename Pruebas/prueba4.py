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
# Inicio de crear Profesional
    def test_Crear_profesional(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("admin")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("admin")
        usuario.send_keys(Keys.ENTER)
        driver.get("http://127.0.0.1:8000/servicios.html")
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/crearProfesionales_N.html")
        self.assertIn("Ingresar Profesional", driver.title)
        rut = driver.find_element_by_id("txtRut")
        rut.send_keys("197927039")
        nombre = driver.find_element_by_id("id_nombre")
        nombre.send_keys("Benjamin")
        paterno = driver.find_element_by_id("id_paterno")
        paterno.send_keys("Bravo")
        materno = driver.find_element_by_id("id_materno")
        materno.send_keys("Ethyl")
        paterno.send_keys(Keys.ENTER)
        time.sleep(2)
        username = driver.find_element_by_id("id_username")
        username.send_keys("Profesionale")
        contraa = driver.find_element_by_id("id_password1")
        contraa.send_keys("duoc123456")
        contras = driver.find_element_by_id("id_password2")
        contras.send_keys("duoc123456")
        email = driver.find_element_by_id("id_email")
        email.send_keys("prueba12@gmail.com")
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        if driver.current_url=='http://127.0.0.1:8000/register_Profesional.html':
            print("Se ha creado el profesional con éxito en el sistema.")
        else:
            print("no se pudo ingresar el profesional")

    def cerrar(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

#login_url = 'https://account.domaintools.com/log-in/?r=https%3A%2F%2Freversewhois.domaintools.com%2F%3Frefine'
#login = driver.find_element_by_xpath('//a[@href="'+login_url+'"]').click()

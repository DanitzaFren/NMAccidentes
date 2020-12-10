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
        usuario.send_keys("Benja")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        #servicio
        driver.find_element_by_xpath('/html/body/header/div/nav/ul/li[4]/a').click()
        time.sleep(2)
        #Crear profesiional
        driver.find_element_by_xpath("/html/body/main/section/div/div/div[2]/div/div[2]/input").click()
        time.sleep(2)
        self.assertIn("Ingresar Profesional", driver.title)
        rut = driver.find_element_by_id("txtRut")
        rut.send_keys("197927035")
        nombre = driver.find_element_by_id("id_nombre")
        nombre.send_keys("Benjami")
        paterno = driver.find_element_by_id("id_paterno")
        paterno.send_keys("Brav")
        materno = driver.find_element_by_id("id_materno")
        materno.send_keys("Dia")
        driver.find_element_by_css_selector("#main > section.contact.aos-init.aos-animate > div > div > div.col-lg-12 > form > center > button").click()
        time.sleep(2)
        username = driver.find_element_by_id("id_username")
        username.send_keys("Profesional6")
        contraa = driver.find_element_by_id("id_password1")
        contraa.send_keys("duoc123456")
        contras = driver.find_element_by_id("id_password2")
        contras.send_keys("duoc123456")
        email = driver.find_element_by_id("id_email")
        email.send_keys("prueba@gmail.com6")
        driver.find_element_by_css_selector("#main > section.contact.aos-init.aos-animate > div > div > div.col-lg-12 > form > center > button").click()
        time.sleep(2)
        if driver.find_element_by_css_selector("#main > section.contact.aos-init.aos-animate > div > div > div.alert.alert-info").text=='Usuario: Profesional registrado correctamente.':
            print("Se a creado el profesional con exito ")
        else:
            print("no se pudo ingresar el profesional")

    def cerrar(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
#login_url = 'https://account.domaintools.com/log-in/?r=https%3A%2F%2Freversewhois.domaintools.com%2F%3Frefine'
#login = driver.find_element_by_xpath('//a[@href="'+login_url+'"]').click()

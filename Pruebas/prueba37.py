import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.chrome.options import Options
class usando_unitest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
#ver Crear capacitacion
    def test_crear_capacitacion(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Profesional")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        #ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a crear Check
        driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[4]/div/div[2]/input").click()
        time.sleep(1)
        #selec fecha
        datefield = driver.find_element_by_name('fecha')
        datefield.click()
        datefield.send_keys("15012021")
        Asistentes = driver.find_element_by_name("asistentes")
        Asistentes.send_keys("10")
        Descripcion = driver.find_element_by_name("descripcion_capa")
        Descripcion.send_keys("Prueba1")
        ####################### luego cambiar a 1
        Seleccionar = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/div/select"))
        Seleccionar.select_by_value("1")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/div/center/button").click()
        time.sleep(10)
        if driver.current_url=='http://127.0.0.1:8000/crearCapacitaciones.html/2':
            print("Se a agregado un nueva capacitacion ")
        else:
            print("Error no se agrego capacitacion")

    def cerrar16(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#ver Crear Visita
    def test_crear_Visita(self):
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
        #ir a crear Visita
        driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[1]/div/div[2]/input").click()
        time.sleep(1)
        #selec fecha
        datefield = driver.find_element_by_name('fecha')
        datefield.click()
        datefield.send_keys("21012021")
        ####################### selec solicitud luego cambiar a 1
        Seleccionar = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/div[2]/select[1]"))
        Seleccionar.select_by_value("1")
        time.sleep(1)
        ######des
        desc = driver.find_element_by_name("descripcion")
        desc.send_keys("Prueba1")
        ####################### selec check
        Seleccionarc = Select(driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/div[2]/select[2]"))
        Seleccionarc.select_by_value("1")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/center/button").click()
        time.sleep(2)
        if driver.find_element_by_xpath("/html/body/main/section[2]/div/div/div/form/div[1]").text=='Visita: Visita Creada':
            print("Se a agregado un nueva visita ")
        else:
            print("Error no se agrego visita")

    def cerrar18(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
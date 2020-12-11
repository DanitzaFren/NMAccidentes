import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#Ver contratos
    def test_ver_contratos_del_sistema(self):
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
        # ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a ver los contratos ingresados 
        driver.find_element_by_xpath("/html/body/main/section/div/div/div[4]/div/div[3]/input").click()
        time.sleep(1)
        if driver.current_url=='http://127.0.0.1:8000/listadoContrato.html':
            print("Se desplego el el listado de los contratos")
        else:
            print("no se despliega los contratos")

    def cerrar6(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
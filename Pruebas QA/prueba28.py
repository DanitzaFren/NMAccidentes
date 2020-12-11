import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#Ingresar ver Checklists del cliente
    def test_Ver_Checklists_del_cliente(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Cliente")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        # ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a ver los Check
        driver.find_element_by_xpath("/html/body/main/section/div/section[1]/div/div/div[4]/div/div[2]/input").click()
        time.sleep(1)
        if driver.current_url=='http://127.0.0.1:8000/listadoChecklistCliente.html/3':
            print("Se desplego el listado de los Checklists ")
        else:
            print("no se desplego el Checklists")

    def cerrar(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
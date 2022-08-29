from lib2to3.pgen2 import driver
import time
import unittest
from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def tearDown(self):
        self.driver.close()


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
    
    def test_search_in_xchrome(self):   
        driver = self.driver
        driver.get("http://www.google.com.co")
        elem = driver.find_element(By.NAME,"q")
        elem.send_keys("Hola esto es una prueba")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Ver todos", driver.page_source)

    def test_search_by_xpath(self):   
        driver = self.driver
        driver.get("http://www.google.com.co")
        elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        elem.send_keys("Hola esto es una prueba")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Ver todos", driver.page_source)


if __name__ == "__main__":
    unittest.main()

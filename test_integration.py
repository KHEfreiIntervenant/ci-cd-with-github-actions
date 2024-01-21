import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class app(unittest.TestCase):
    def setUp(self):
        # Launch your flask app first
        chrome_options = Options()
        chrome_options.binary_location= 'C:\\Users\\Shawn\\mlinprod\\chromedriver'
        self.driver = webdriver.Chrome()
        self.driver.get('https://ee0e-2a02-842b-c2-7001-84a7-f1a6-e06-6bb5.ngrok-free.app')

    def test_add_and_delete_item(self):
        # you can use the driver to find elements in the page
        # example:
        wait = WebDriverWait(self.driver, 10)
        input_field = wait.until(EC.presence_of_element_located((By.NAME, 'item')))
        # this refers to the 'name="item"' attribute of the html element
        # checkout the rest of the methods in the documentation:
        # https://selenium-python.readthedocs.io/locating-elements.html
        
        # after you select your element, you can send it a key press:
        input_field.send_keys('New E2E Item')
        input_field.send_keys(Keys.RETURN)
        
        # and you can use the rest of the assetion methods as well:
        self.assertIn('New E2E Item', self.driver.page_source)
        
        # Testing Update operation
        update_form = self.driver.find_element(By.NAME, 'new_item')
        update_form.send_keys('Updated E2E Item'+Keys.RETURN)
        self.assertIn('Updated E2E Item', self.driver.page_source)
        self.assertNotIn('New E2E Item', self.driver.page_source)

        # Testing Delete operation
        delete_item = self.driver.find_element(By.LINK_TEXT, 'Delete')
        delete_item.click()
        self.assertNotIn('New E2E Item', self.driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

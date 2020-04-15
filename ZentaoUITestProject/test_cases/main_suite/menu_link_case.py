import os
import time
import  unittest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import set_driver
from common import login

# chrome_path=os.getcwd()+'/../../webdriver/chromedriver.exe'
class MainLinkCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    def test_my_link(self):
        '''验证我的地盘菜单能否正确链接'''
        login.login(self.driver, 'test01', 'newdream123')
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        WebDriverWait(self.driver,10).until(EC.title_is('我的地盘 - 禅道'))
    def test_product_link(self):
        '''验证产品菜单能否正确链接'''
        login.login(self.driver, 'test01', 'newdream123')
        self.driver.find_element(By.XPATH,'//li[@data-id="product"]').click()
        WebDriverWait(self.driver,10).until(EC.title_is('产品主页 - 禅道'))

if __name__=='__main__':
    unittest.main()
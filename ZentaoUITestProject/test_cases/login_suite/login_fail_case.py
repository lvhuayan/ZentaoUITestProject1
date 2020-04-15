import os
import time
import  unittest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

# chrome_path=os.getcwd()+'/../../webdriver/chromedriver.exe'
class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    def test_login_fail(self):
        '''使用错误密码测试能否登录'''
        login.login(self.driver, 'test01', 'newdream1')
        time.sleep(2)
        self.assertTrue(WebDriverWait(self.driver,10).until(EC.alert_is_present()))
if __name__=='__main__':
    unittest.main()
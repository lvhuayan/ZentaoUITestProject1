import os
import time
import  unittest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login

# chrome_path=os.getcwd()+'/../../webdriver/chromedriver.exe'
class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver =set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    def test_login_1(self):
        '''使用case01  newdream123 测试能否登录'''
        login.login(self.driver,'test01','newdream123')
        actual_result=self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        # self.assertEqual(actual_result,'测试人员1','test_login用例执行失败')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'//span[@class="user-name"]'),'测试人员01'),'test_login用例执行失败')
    def test_login_2(self):
        '''使用case02 newdream123 测试能否登录'''
        login.login(self.driver, 'test02', 'newdream123')
        actual_result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        self.assertEqual(actual_result, '测试人员2', 'test_login用例执行失败')
if __name__=='__main__':
   unittest.main()
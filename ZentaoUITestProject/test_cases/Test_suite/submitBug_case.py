import os
import time
import  unittest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import set_driver
from common import login
from common import submit_bug

# chrome_path=os.getcwd()+'/../../webdriver/chromedriver.exe'
class SubmitBugCases(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    def test_submit_Bug(self):
        '''提交bug'''
        login.login(self.driver, 'test01', 'newdream123')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//a[contains(@href,"/zentao/www/index.php?m=qa&f")]').click()
        self.driver.find_element(By.XPATH, '//a[contains(@href,"/zentao/www/index.php?m=bug")]').click()
        self.driver.find_element(By.XPATH, '//a[contains(@href,"/zentao/www/index.php?m=bug&f=create")]').click()
        submit_bug.submit_bug(self.driver,'2020-4-14','2020-4-14提交的bug','步骤：。。。')
if __name__=='__main__':
    unittest.main()
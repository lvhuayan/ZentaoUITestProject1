from selenium import webdriver

def set_driver():
    driver = webdriver.Chrome()  # executable_path=chrome_path
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    return driver
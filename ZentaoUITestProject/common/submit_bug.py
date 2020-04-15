import time
from selenium.webdriver.common.by import By
def submit_bug(driver,date,bug_title,bug_step):
    # 提bug
    driver.find_element(By.XPATH, '//div[@id="product_chosen"]').click()  # 所属产品
    driver.find_element(By.XPATH, '//li[@title="学生成绩管理系统"]').click()

    driver.find_element(By.XPATH, '//div[@id="module_chosen"]').click()  # 所属模块
    driver.find_element(By.XPATH, '//li[@title="/年级成绩管理"]').click()

    driver.find_element(By.XPATH, '//div[@id="project_chosen"]').click()  # 所属项目
    driver.find_element(By.XPATH, '//li[@title="湖南工业职院17测试实训"]').click()

    time.sleep(2)
    driver.find_element(By.XPATH, '//div[@id="openedBuild_chosen"]').click()  # 影响版本
    driver.find_element(By.XPATH, '//li[@title="主干"]').click()

    driver.find_element(By.XPATH, '//div[@id="assignedTo_chosen"]').click()  # 当前指派
    driver.find_element(By.XPATH, '//li[@title="D:开发人员1"]').click()

    driver.find_element(By.XPATH, '//input[@id="deadline"]').send_keys(date)  # 截止日期

    driver.find_element(By.XPATH, '//div[@id="type_chosen"]').click()  # bug类型
    driver.find_element(By.XPATH, '//li[@title="性能问题"]').click()

    driver.find_element(By.XPATH, '//div[@id="os_chosen"]').click()  # 操作系统
    driver.find_element(By.XPATH, '//li[@title="Windows 2008"]').click()

    driver.find_element(By.XPATH, '//div[@id="browser_chosen"]').click()  # 浏览器
    driver.find_element(By.XPATH, '//li[@title="IE7"]').click()

    driver.find_element(By.XPATH, '//input[@id="title"]').send_keys(bug_title)  # bug标题

    driver.find_element(By.XPATH, '//div[@class="input-group-btn pri-selector"]').click()  # 严重程度
    driver.find_element(By.XPATH, '//span[@data-value="4"]').click()

    driver.find_element(By.XPATH, '//div[@data-type="pri"]').click()  # 优先级
    driver.find_element(By.XPATH, '//span[@data-value="4" and @class="label label-pri"]').click()

    element = driver.find_element(By.XPATH, '//iframe[@class="ke-edit-iframe"]')
    driver.switch_to.frame(element)
    driver.find_element(By.XPATH, '//body[@class="article-content"]').clear()  # 重现步骤
    driver.find_element(By.XPATH, '//body[@class="article-content"]').send_keys(bug_step)
    driver.switch_to.default_content()

    element1 = driver.find_element(By.XPATH, '//div[@id="mailto_chosen"]')  # 抄送给
    driver.execute_script('arguments[0].scrollIntoView();', element1)  # 元素被挡住时下滑到此元素
    element1.click()
    driver.find_element(By.XPATH, '//div[@id="mailto_chosen"]/div/ul/li[@title="T:测试人员1"]').click()

    driver.find_element(By.XPATH, '//button[@id="submit"]').click()  # 保存

    time.sleep(3)

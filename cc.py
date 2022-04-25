from selenium import webdriver
import time
# Chrome浏览器
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime


def create_chrome_driver(flag):
    if flag == 'chrome':
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        option.add_experimental_option("detach", True)
        # 无头浏览器需要添加user-agent来隐藏特征
        option.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36')
        chrome_driver = Chrome(options=option)
        chrome_driver.implicitly_wait(5)
        with open('stealthFile/stealth.min.js') as f:
            js = f.read()
        chrome_driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {
                "source": js})
        return chrome_driver
    else:
        option = webdriver.FirefoxOptions()
        fire_driver = Firefox(options=option)
        fire_driver.implicitly_wait(5)
        with open('stealthFile/stealth.min.js') as f:
            js = f.read()
        fire_driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument", {
                "source": js})
        return fire_driver


driver = create_chrome_driver('chrome')
action = ActionChains(driver)
driver.get('https://taobao.com/')


def get_btn(xpath):
    btn = driver.find_element(By.XPATH, xpath)
    return btn


def move_dom(obj, tim):
    action.move_to_element(obj).perform()
    time.sleep(tim)


def click_dom(tim):
    action.click().perform()
    time.sleep(tim)


time.sleep(3.6)
driver.maximize_window()

# 找到登录按钮
login_btn = driver.find_element(
    By.XPATH, '//div[@class="site-nav-menu-hd"]/div[@class="site-nav-sign"]/a[1]')
time.sleep(3)
action.move_to_element(login_btn).perform()
time.sleep(1.3)
action.click().perform()
time.sleep(3)
# action.context_click().perform()

btn1 = driver.find_element(By.XPATH, '//div[@id="login"]/div/i[1]')
action.move_to_element(btn1).perform()
time.sleep(1)

action.click().perform()

driver.implicitly_wait(40)
try:
    btn2 = driver.find_element(
        By.XPATH, '//div[@class="member-column-4"]/a[1]')
except Exception as e:
    print(e)
    print(f'耗时：')

time.sleep(2)
shop_car_btn = driver.find_element(By.XPATH, '//li[@id="J_MiniCart"]/div/a')
action.move_to_element(shop_car_btn).perform()
time.sleep(2)
action.click().perform()
time.sleep(3)
action.move_to_element(
    driver.find_element(
        By.XPATH,
        '//div[@id="J_SelectAll1"]')).perform()
time.sleep(1.3)
click_dom(3)

btn_go = get_btn('//a[@id="J_Go"]')
move_dom(btn_go, 2.3)

click_dom(0.1)

driver.implicitly_wait(3)
try:
    driver.find_element(By.XPATH, '//div/a[@class="go-btn"]').click()
    print(666666666666666666666)
except Exception as e:
    print(e)


one = datetime.now()
two = datetime.datetime.hour(20)

print(one, two)
# driver.close()

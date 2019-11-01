from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'OPPO',
    'platformVersion': '8.1.0',
    'appPackage': 'com.bill99.kuaiqian',
    'appActivity': 'com.bill99.kuaiqian.SplashActivity',
    'unid': 'de6cd069',
    'noReset': 'true',
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


time.sleep(3)
driver.quit()
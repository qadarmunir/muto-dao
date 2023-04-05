from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
import selenium_metamask_automation
from webdriver_manager.chrome import ChromeDriverManager

EXTENSION_PATH =  r"C:\Windows.old\Users\Arhamsoft\AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\10.14.6_0.crx"

def launchSeleniumWebdriver(driverpath):
    print('path', EXTENSION_PATH)
    chrome_options = Options()
    chrome_options.add_extension(EXTENSION_PATH)
    global driver
    driver = webdriver.Chrome(options=chrome_options, executable_path=driverpath) 
    time.sleep(5)
    print("Extension has been loaded")
    return driver

def metamaskSetup(recoveryPhrase, password):
    driver.switch_to.window(driver.window_handles[0])
    sleep(5)

    driver.find_element_by_xpath('//button[text()="Get Started"]').click()
    driver.find_element_by_xpath('//button[text()="Import wallet"]').click()
    driver.find_element_by_xpath('//button[text()="No Thanks"]').click()

    time.sleep(5)

    inputs = driver.find_elements_by_xpath('//input')
    inputs[0].send_keys(recoveryPhrase)
    inputs[1].send_keys(password)
    inputs[2].send_keys(password)
    driver.find_element_by_css_selector('.first-time-flow__terms').click()
    driver.find_element_by_xpath('//button[text()="Import"]').click()

    time.sleep(5)

    driver.find_element_by_xpath('//button[text()="All Done"]').click()
    time.sleep(2)

    # closing the message popup after all done metamask screen
    driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
    time.sleep(2)
    print("Wallet has been imported successfully")
    time.sleep(10)
selenium_metamask_automation.launchSeleniumWebdriver("C:\Users\Arhamsoft\Downloads\chromedriver_win32\chromedriver.exe")
selenium_metamask_automation.metamaskSetup(["gospel", "gold", "stone", "party", "evolve", "hungry", "mandate", "exile", "coach", "cupboard", "exit", "budget"], "qadar4646", )

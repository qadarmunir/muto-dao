import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.keys import Keys
from time import sleep
import asyncio
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
 
def run_chrome():
    
    #criando uma instância do chrome com o profile escolhido    
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("user-data-dir=C:\\Python")
    driver = webdriver.Chrome(options=options)
    ac = ActionChains(driver)
    
    #abrindo o metamask e logando
    driver.get('nkbihfbeogaeaoehlefnkodbefgpgknn')
    delay = 3 # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    s_pass = "qadar4646"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(s_pass)
    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[4]/div/div/button/span').click()
    
    #abrindo uma nova guia com o metamaks
    EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
    
    
    
    #abrindo o PvU
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://mutodao.metamuto.com/')
    
    #I CAN'T PASS THIS 

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/img')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        content = driver.find_element(By.CSS_SELECTOR,"div.metamask.tw-flex.tw-items-center.tw-p-3.tw-cursor-pointer")
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
    content.click()
    element = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.metamask.tw-flex.tw-items-center.tw-p-3.tw-cursor-pointer")))
    ac.move_to_element(element).click(element).perform()
    
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    
run_chrome()
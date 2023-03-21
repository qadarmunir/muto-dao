from selenium import webdriver
import time 
from selenium.webdriver.chrome.options  import Options
import os
import urllib.request

EXTENSHION_PATH = os.getcwd() + 'metamaskExtenshion.crx'
EXTENSHION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

def Dolwnload_metamask():
    print('setting up metamask extenshion please wait...')

    url = 'https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn'
    urllib.request.urlretrieve(url, os.getcwd() + 'metamaskExtenshion.crx')
def lunchSeleniumWebdriver(driverpath):
    print('path', EXTENSHION_PATH)
    chrome_options =Options()
    chrome_options.add_extenshion(EXTENSHION_PATH)
    global driver
    driver =webdriver.Chrome(otions=chrome_options, executable_path =driverpath)
    time.sleep(5)
    print("Extenshion has been loaded")
    return driver
def metamasketup(recoverphrase, password):
    driver.switch_to.window(driver.window_handles[0])

    driver.find_element_by_xpath("//button[text()="Get Started"]").click()
    driver.find_element_by_xpath("//button[text()="Import wallet"]").click()
    driver.find_element_by_xpath("//button[text()="No Thanks"]").click()

    time.sleep(5)

    input= driver.find_elements_by_xpath('//input')
    input[0].send_keys(recoveryPhrase)
    input[1].send_keys(password)
    input[2].send_keys(password)
    driver.find_element_by_css_selector(".first-time-flow__terms").click()
    driver.find_element_by_xpath("//button[text()="Import"]").click()

    time.sleep(5)

    driver.find_element_by_xpath("//*[@id="popover-content"]/div/div/section/header/div/button").click()
    time.sleep(2)
    print("wallet has imported successfully")
    time.sleep(10)

    #change maetamask network to rinkeby
def Change_metaMask_network(networkname):
        #opening network
        print("changing metmask network")
        driver.switch_to.window(driver.window_handle[1])
        driver.get('chrome-extension://{}/home.html'.format(EXTENSHION_ID))
        print("cliosing popup")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id="popover-content"]/div/div/section/header/div/button").click()
        driver.find_element_by_css_selector("//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span").click()

        time.sleep(2)
        print("opening network dropdown")
        elem = driver.find_element_by_xpath("//*[@id="app-content"]/div/div[3]/div")
        time.sleep(2)
        all_li= elem.find_elements_by_tag_name("li")
        time.sleep(5)
        for li in all_li:
            text= li.text
            if (text == networkName):
                li.click()
                print(text, "is selected")
                time.sleep(5)
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5)
                return
        time.sleep(2)
        print("please provide a valid network name")

        driver.switcj_to.window(driver.window_handles[0])
        time.sleep(3)
#connect to website 
def connectToWebsite():
    time.sleep(3)
    driver.execute_sciript("window.open('');")  
    driver.switch_to.window(driver.window_handles[1])

    driver.get("chrome-extension://{}/popup.html".format(EXTENSHION_ID))
    time.sleep(5) 
    driver.execute_script("window.scrollBy(0, document.body.scrolHeight)") 
    time.sleep(3)

    driver.find_element_by_xpath("//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]").click()
    time.sleep(5)
    print("site connected to metamask successfully")
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)

def confirmapprovalfrommetamask():
     driver.execute_script("window.open(''):")
     driver.switch_to.window(driver.window_handles[1])

     driver.get('chrome-extenshion://{}/popup.html'.format(EXTENSHION_ID))
     time.sleep(10)

     #confirm approval from matemask
     driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]').click()
     time.sleep(12)
     print("approval confirmed from metamask")

     #switch to dafi 
     driver.switch_to.window(driver.window_handles[0])
     time.sleep(3)

def rejectapprovalfrommetamask():
     driver.execute.sciript("window.open(');")
     driver.switch_to.window(driver.window_handles[1])

     driver.get('chrome-extenshion://{}/popup.html'.format(EXTENSHION_ID))
     time.sleep(10)
     driver.execute_script("window.scroll(0, document.body.scrollHeight)")
     time.sleep(10)

     #comfirm approval from matemask
     driver.find_element_by_xpath("//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[1]").click()
     time.sleep(8)
     print("approval rejected from metamask")

     #switch to daFi
     driver.switch_to.window(driver.window_handles[0])  
     time.sleep(3)
     print("reject approval from metamask")
def  confirmtransectionfrommetamask():
     driver.execute_sciript("window.open(');")
     driver.switch_to.window(driver.window_handles[1])

     driver.get('chrome-extension://{}/popup.html'.format(EXTENSHION_ID)) 
     time.sleep(10)
     driver.execute_sciript("window.scroll(0, document.body.scrollHeight)")
     time.sleep(10)
#confirm transection from metamask
     driver.find_element_by_xpath("//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]").click()
     time.sleep(13)
     print("transection confirmed") 

     #switch to dafi
     driver.switch_to.window(driver.window_handles[0])
     time.sleep(3)
def rejecttransectionfrommetamask():
     driver.execute_script("window.open('');")
     driver.switch_to.window(driver.window_handles[1])

     driver.get('chrome-extension://{}/popup.html'.format(EXTENSHION_ID))
     time.sleep(5)
     driver.execute_script("window.scroll(0, document.body.scrollHeight)")
     time.sleep(5)

     #confirm approval from metamask
     driver.find_element_by_xpath("//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[1]").click()
     time.sleep(2)
     print("transection rejected")

     #sswitch to web window
     driver.switch_to.window(driver.window_handles[0])
     time.sleep(3)

def addtoken(tokenAddress):
     #open metamask
    print("adding token")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('chrome-extension://{}/home.html'.format(EXTENSHION_ID))
    print("cliosing popup")
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id="popover-content"]/div/div/section/header/div/button").click()
    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span').click()
    # time.sleep(2)
    
    print("clicking add token button")    
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div/div/div[3]/div/div[3]/button').click()
    time.sleep(2)

    #adding address
    driver.find_element_by_id("custom-address").send_keys(tokenAddress)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[2]/div[2]/footer/button[2]').click()
    time.sleep(2)
    # add tokens
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[3]/footer/button[2]').click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    print("token added successfully")

def signConfirm():
    print("sign")
    time.sleep(3)

    driver.execute_sciript("window.open('');")  
    driver.switch_to.window(driver.window_handles[1])

    driver.get("chrome-extension://{}/popup.html".format(EXTENSHION_ID))
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, document.body.scrolHeight)")
    time.sleep(3)
    #driver.find_element_by_xpath("//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]").click()
    #time.sleep(3)
    print('sign confirmed')
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

    #reject sign
def signReject():
    print("sign")
    time.sleep(3)
    
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

    driver.get("chrome-extension://{}/popup.html".format(EXTENSHION_ID))
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/button[1]').click()
    time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    # time.sleep(3)
    print('sign rejected')
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)






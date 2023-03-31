from selenium import webdriver

EXTENSION_PATH ="C:\Windows.old\Users\Arhamsoft\AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\10.14.6_0.crx"
sleep(25)
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)

driver = webdriver.Chrome(chrome_options=opt)
driver.find_element_by_xpath('//button[text()="Get Started"]').click()
driver.find_element_by_xpath('//button[text()="Import wallet"]').click()
driver.find_element_by_xpath('//button[text()="No Thanks"]').click()

# After this you will need to enter you wallet details

inputs = driver.find_elements_by_xpath('//input')
inputs[0].send_keys("gospel", "gold", "stone", "party", "evolve", "hungry", "mandate", "exile", "coach", "cupboard", "exit", "budget")
inputs[1].send_keys("qadar4646")
inputs[2].send_keys("qadar4646")
driver.find_element_by_css_selector('.first-time-flow__terms').click()
driver.find_element_by_xpath('//button[text()="Import"]').click()
driver.find_element_by_xpath('//button[text()="All Done"]').click()
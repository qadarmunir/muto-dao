from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome driver with MetaMask extension
options = webdriver.ChromeOptions()
options.add_extension(r"C:\Windows.old\Users\Arhamsoft\AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\10.14.6_0.crx")
driver = webdriver.Chrome(options=options)

# Open website
driver.get('https://testnet.elumnt.com/')
driver.maximize_window()
connect_wallet= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(@type,'button')])[6]")))
connect_wallet.click()
signin_metamask= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div)[21]")))
signin_metamask.click()

# Switch to MetaMask window
driver.switch_to.window(driver.window_handles[-1])

# Wait for MetaMask to load
###WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Get Started')]"))).click()
 
getstarted= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '//button[text()="Get Started"]')))
getstarted.click()
import_wallet= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '//button[text()="Import wallet"]')))
import_wallet.click()
no_thanks= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '//button[text()="No Thanks"]')))
no_thanks.click()


inputs=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '//input')))
inputs[0].send_keys("gospel", "gold", "stone", "party", "evolve", "hungry", "mandate", "exile", "coach", "cupboard", "exit", "budget")
inputs[1].send_keys("qadar4646")
inputs[2].send_keys("qadar4646")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '.first-time-flow__terms'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '//button[text()="Import"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '//button[text()="All Done"]'))).click()
# closing the message popup after all done metamask screen
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '//*[@id="popover-content"]/div/div/section/header/div/button'))).click()    
print("Wallet has been imported successfully")

# Send password to MetaMask
# password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
# password_field.send_keys("qadar4646")
# submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
# submit_button.click()

# Confirm transaction
confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm')]")))
confirm_button.click()

# Switch back to main window
driver.switch_to.window(driver.window_handles[0])

#send keys to the app like name email and password
name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='exampleForm.ControlInput1'])[1]")))
name.send_keys("umair_khan")
fullname = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='exampleForm.ControlInput1'])[2]")))
fullname.send_keys("omairkhan")
email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='exampleForm.ControlInput1'])[3]")))
email.send_keys("qadar00111@gamil.com")

#click on check box
check_box1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span)[17]")))
check_box1.click()
check_box2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span)[18]")))
check_box2.click()
#finish signup button
finish_signup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-outline-warning finish-btn")))
finish_signup.click()
# Switch to MetaMask window
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Get Started')]")))

# # Send password to MetaMask
# password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
# password_field.send_keys("qadar4646")
# submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
# submit_button.click()

# # Confirm transaction
# confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm')]")))
# confirm_button.click()

# # Switch back to main window
# driver.switch_to.window(driver.window_handles[0])driver.switch_to.window(driver.window_handles[-1])

# Wait for MetaMask to load

#click on create button
create_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button)[3]")))
create_button.click()
#select network
select_network = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "")))
select_network.click()
#select single/multiple
select_single = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span)[19]")))
select_single.click()
# Click create NFT button
create_nft_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div)[28]")))
create_nft_button.click()

# Fill in NFT creation form
name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@id='name'])[1]")))
name_field.send_keys("My NFT")
description_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//textarea[@placeholder='Example: “The #2 NFT of the Elumnt PFP Collection”'])[1]")))
description_field.send_keys("Description of my NFT")
image_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span)[19]")))
image_field.send_keys("dogc 3.0.png")
price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Example: 1.3'])[1]")))
price.send_keys("0.0003")

royalties = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Example:0%,10%,30%,Maximum is 50%'])[1]")))
royalties.send_keys("10")

# Submit NFT creation form
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[9]")))
submit_button.click()

# Confirm transaction
confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm')]")))
confirm_button.click()

# Switch back to MetaMask window
driver.switch_to.window(driver.window_handles[-1])

# Confirm transaction in MetaMask
confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm')]")))
confirm_button.click()

# Switch back to main window
driver.switch_to.window(driver.window_handles[0])

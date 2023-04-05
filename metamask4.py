from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome driver with MetaMask extension
options = webdriver.ChromeOptions()
options.add_extension(r"C:\Windows.old\Users\Arhamsoft\AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\10.14.6_0.crx")
driver = webdriver.Chrome(options=options)

# Open website
driver.get("https://testnet.elumnt.com/")

# Click sign in button
sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]")))
sign_in_button.click()

# Switch to MetaMask window
driver.switch_to.window(driver.window_handles[-1])

# Wait for MetaMask to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Get Started')]")))

# Send password to MetaMask
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
password_field.send_keys("qadar4646")
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
submit_button.click()

# Confirm transaction
confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm')]")))
confirm_button.click()

# Switch back to main window
driver.switch_to.window(driver.window_handles[0])

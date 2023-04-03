from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# Set the path to the Metamask extension file
EXTENSION_PATH = r"C:\Windows.old\Users\Arhamsoft\AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\10.14.6_0.crx"

# Set up ChromeOptions with Metamask extension
options = Options()
options.add_extension(EXTENSION_PATH)
# Launch Chrome with the Metamask extension
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# Navigate to a webpage where you want to interact with Metamask
driver.get("https://testnet.elumnt.com/")
driver.find_element_by_xpath("//button[@type='button'])[5]").click()
driver.find_element_by_xpath('//button[text()="Import wallet"]').click()

# Find the Metamask extension button on the browser toolbar and click it
metamask_button = driver.find_element_by_xpath("//button[@aria-label='MetaMask']")
metamask_button.click()

# Wait for the Metamask extension popup to load
popup_xpath = "//div[@class='popup-content']"

wait.until(EC.presence_of_element_located((By.XPATH, popup_xpath)))

# Once the popup has loaded, locate and interact with the elements within it
# For example, you can find and click the "Connect" button:
connect_button_xpath = "//button[contains(text(),'Connect')]"
connect_button = driver.find_element_by_xpath(connect_button_xpath)
connect_button.click()
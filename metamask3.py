from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Specify the path to the Metamask extension
EXTENSION_PATH = r"C:\Windows.old\Users\Arhamsoft\AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\10.14.6_0.crx"

# Set up the Chrome options to add the extension
chrome_options = Options()
chrome_options.add_extension(EXTENSION_PATH)

# Launch the Chrome browser with the Metamask extension
driver = webdriver.Chrome(options=chrome_options)

# Navigate to a website
driver.get("https://testnet.elumnt.com/login")

# Wait for the Metamask extension to load
wait = WebDriverWait(driver, 25)
#signin = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'])[5]")))
#click on sign in metamask
connect_wallet= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "login-btn btn btn-primary")))
connect_wallet.click()
signin_metamask= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mb-0")))
signin_metamask.click()
#send keys to the app like name email and password
name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='exampleForm.ControlInput1'])[1]")))
name.send_keys("umair_khan")
fullname = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='exampleForm.ControlInput1'])[2]")))
fullname.send_keys("omairkhan")
email = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='exampleForm.ControlInput1'])[3]")))
email.send_keys("qadar00111@gamil.com")

#click on check box
check_box1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span)[17]")))
check_box1.click()
check_box2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span)[18]")))
check_box2.click()


metamask_logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='app-header__logo-container']")))

# Click the Metamask logo to open the extension
metamask_logo.click()

# Wait for the Metamask extension popup to appear
metamask_popup = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='popover-header__container']")))

# Click the "Get Started" button
get_started_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Get Started']")))
get_started_btn.click()

# Click the "Sign In" button
sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign In']")))
sign_in_btn.click()

# Switch to the Metamask popup window
driver.switch_to.window(driver.window_handles[-1])

# Confirm the connection request
confirm_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='first-time-flow__button']")))
confirm_btn.click()

# Scroll the Metamask popup window
popup_body = driver.find_element(By.XPATH, "//body[@class='modal-open']")
ActionChains(driver).move_to_element(popup_body).perform()
popup_body.send_keys(Keys.PAGE_DOWN)

# Switch back to the original window
driver.switch_to.window(driver.window_handles[0])

# Close the browser window
driver.quit()

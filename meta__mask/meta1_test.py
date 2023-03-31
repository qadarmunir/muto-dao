from selenium import webdriver

EXTENSION_PATH ="C:\Windows.old\Users\Arhamsoft\AppData\Local\Google\Chrome\User Data\Default\Extensions\nkbihfbeogaeaoehlefnkodbefgpgknn\10.14.6_0.crx"
sleep(25)
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)

driver = webdriver.Chrome(chrome_options=opt)
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
import urllib.request


EXTENSION_PATH = os.getcwd() + '\metamaskExtension.crx'   #os.getcwd() method returns the current working directory, and the string
                                                          #.crx represents  the extension of the metamask  google chroome extension

EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'         #meta mask extenshion id, which we can find in link of metamask extenshion

import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import os


#@pytest.fixture(scope="class")
#def browser():
    #print('Start test')
    #options = Options()
    #options.add_argument("--headless=new")
    #options.add_argument("--no-sandbox")
    #options.add_argument("--disable-dev-shm-usage")
    #options.add_argument("--window-size=1920,1080")
    #options.page_load_strategy = 'normal'
    #river_path = ChromeDriverManager().install()
    #if driver_path:
    #    driver_name = driver_path.split('/')[-1]
    #    if driver_name!="chromedriver":
    #       driver_path = "/".join(driver_path.split('/')[:-1]+["chromedriver.exe"])
    #        os.chmod(driver_path, 0o755)
    #driver = webdriver.Chrome(options=options, service=Service(driver_path))
    #driver.get("https://stage-lti.softline.com/")
    #yield driver
    #driver.quit()
    #print('Finish test')

@pytest.fixture(scope="package")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

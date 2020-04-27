from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait #check if page is loaded and ready
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.accuweather.com/")
def searchForLocation(location):
    driver.find_element_by_name("query").send_keys("cairo")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[1]/svg[1]/path")

searchForLocation("egypt")


driver.close()
driver.quit()
#hey man this is absolutely amazing!
#yup, works like a chramr
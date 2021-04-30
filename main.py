# Import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random,time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/")
print(driver.title)

channel_list = ['code with harry','apna college','corey schafer','keith galli','programming hero','freecodecamp','dev ed','telusko','python programmer','kalle hallden','tech with tim','apni kaksha','aman dhattarwal','comicverse']
channel = random.choice(channel_list)

time.sleep(5)

def search_query():
    search_query = driver.find_element_by_name('search_query')
    search_query.send_keys(channel)

search_query()
time.sleep(4)

def search_click():

    search_btn = driver.find_element_by_id("search-icon-legacy")
    search_btn.click()

search_click()
time.sleep(4)


if __name__ == "__main__":

    driver.quit()
    print("Code Completed 🔥")
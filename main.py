# Import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/")
print(driver.title)










if __name__ == "__main__":

    print("Code Completed 🔥")
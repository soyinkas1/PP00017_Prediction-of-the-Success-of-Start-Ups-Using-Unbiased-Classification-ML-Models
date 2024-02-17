# Import the required libraries
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataCleaningConfig, DataScrappingConfig


try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # Adding argument to disable the AutomationControlled flag
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Exclude the collection of enable-automation switches
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # Turn-off userAutomationExtension
    options.add_experimental_option('useAutomationExtension', False)
    service = Service(executable_path='D:\OneDrive\Documents\PERSONAL\PERSONAL DEVELOPMENT\DATA SCIENCE\Personal Project Portfolio\PP00017_Prediction of the Success of Start-Ups Using Unbiased Classification ML Models\src\chromedriver.exe')
    # self.scraper_config.chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://www.timeshighereducation.com/world-university-rankings/2024/world-ranking?cmp=1#!/length/-1/sort_by/rank/sort_order/asc/cols/stats')
    driver.maximize_window()
    time.sleep(10)
except:
    # driver.quit()
    print('error1')

try:
    
    scores_tab = driver.find_element(By.XPATH, './/label[@for="scores"]')
    driver.execute_script("arguments[0].click();", scores_tab)
    print('clicked')

    rank = []
    rank_name = []
    country = []
    overall = []


    # find the table rows
    time.sleep(10)
    matches = WebDriverWait(driver, 8).until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))

    # matches = driver.find_elements(By.TAG_NAME, 'tr')
    print(len(matches))
  
    for match in matches:
        # rank.append(match.text)
        rank = match.text.split('\n')
        rank_name.append(rank[0])
        country.append(rank[1])
        # overall.append(rank[2])

    df = pd.DataFrame({'rank_name':rank_name, 'country': country } )
    df.to_csv('test.csv', index=False)
    print(df.head(5))

except Exception as e:
    raise CustomException(e, sys)


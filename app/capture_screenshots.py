#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

os.makedirs('screenshots', exist_ok=True)

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
driver.set_window_size(1400, 1000)

BASE_URL = 'http://127.0.0.1:5001'

try:
    # Homepage
    driver.get(BASE_URL)
    time.sleep(2)
    driver.save_screenshot('screenshots/01_homepage.png')
    print('01_homepage.png')
    
    # Positive
    text_input = driver.find_element(By.ID, 'textInput')
    text_input.clear()
    text_input.send_keys('I absolutely love this application!')
    time.sleep(1)
    driver.save_screenshot('screenshots/02_positive_input.png')
    print('02_positive_input.png')
    
    driver.find_element(By.ID, 'analyzeBtn').click()
    time.sleep(4)
    driver.save_screenshot('screenshots/03_positive_results.png')
    print('03_positive_results.png')
    
    # Negative
    text_input.clear()
    text_input.send_keys('This is terrible and useless!')
    time.sleep(1)
    driver.save_screenshot('screenshots/04_negative_input.png')
    print('04_negative_input.png')
    
    driver.find_element(By.ID, 'analyzeBtn').click()
    time.sleep(4)
    driver.save_screenshot('screenshots/05_negative_results.png')
    print('05_negative_results.png')
    
    # Neutral
    text_input.clear()
    text_input.send_keys('The weather is nice today.')
    time.sleep(1)
    driver.save_screenshot('screenshots/06_neutral_input.png')
    print('06_neutral_input.png')
    
    driver.find_element(By.ID, 'analyzeBtn').click()
    time.sleep(4)
    driver.save_screenshot('screenshots/07_neutral_results.png')
    print('07_neutral_results.png')
    
    # File Upload
    driver.find_element(By.XPATH, "//button[@data-tab='file-upload']").click()
    time.sleep(1)
    driver.save_screenshot('screenshots/08_file_upload_tab.png')
    print('08_file_upload_tab.png')
    
    driver.find_element(By.ID, 'fileInput').send_keys(os.path.abspath('sample_movie_review.txt'))
    time.sleep(2)
    driver.save_screenshot('screenshots/09_file_selected.png')
    print('09_file_selected.png')
    
    time.sleep(1)
    driver.save_screenshot('screenshots/10_movie_review_results.png')
    print('10_movie_review_results.png')
    
    # Batch
    driver.find_element(By.XPATH, "//button[@data-tab='batch-analysis']").click()
    time.sleep(1)
    driver.save_screenshot('screenshots/11_batch_tab.png')
    print('11_batch_tab.png')
    
    batch_input = driver.find_element(By.ID, 'batchInput')
    batch_input.clear()
    batch_input.send_keys('I love this!\n\nTerrible!\n\nNice!')
    time.sleep(1)
    driver.save_screenshot('screenshots/12_batch_input.png')
    print('12_batch_input.png')
    
    driver.find_element(By.ID, 'batchAnalyzeBtn').click()
    time.sleep(4)
    driver.save_screenshot('screenshots/13_batch_results.png')
    print('13_batch_results.png')
    
    # Character counter
    driver.find_element(By.XPATH, "//button[@data-tab='text-input']").click()
    time.sleep(1)
    text_input = driver.find_element(By.ID, 'textInput')
    text_input.clear()
    text_input.send_keys('A' * 2500)
    time.sleep(1)
    driver.save_screenshot('screenshots/14_char_counter.png')
    print('14_char_counter.png')
    
    # Error
    text_input.clear()
    time.sleep(0.5)
    driver.find_element(By.ID, 'analyzeBtn').click()
    time.sleep(1)
    driver.save_screenshot('screenshots/15_empty_error.png')
    print('15_empty_error.png')
    
    print('All 15 screenshots captured!')
    
finally:
    driver.quit()

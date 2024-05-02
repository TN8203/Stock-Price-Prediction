from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import csv

options = webdriver.ChromeOptions()
driver = uc.Chrome()

site_aapl = 'http://www.nasdaq.com/symbol/aapl/news-headlines?page='

# Open the CSV file for writing
with open('url_raw.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])  # Write the header row
    
    # Variable to keep track of the number of URLs collected
    url_count = 0
    
    # Iterate through the pages of the website to collect URLs
    for i in range(1, 51):  # Collect from page 1 to page 50
        # Construct the URL for the current page
        webpage = site_aapl + str(i)
        
        # Open the webpage
        driver.get(webpage)
        
        # Find all links with class "jupiter22-c-article-list__item_title"
        links = driver.find_elements(By.CLASS_NAME, 'jupiter22-c-article-list__item_title')
        
        # Extract URLs from the links and write them directly to the CSV file
        for link in links:
            url = link.get_attribute('href')
            writer.writerow([url])
            url_count += 1
            
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.com/Foldable-Adjustable-Holder-Compatible-iPhone/dp/B0B42BNLQ7?ref=dlx_deals_gd_dcl_img_5_e77c9844_dt_sl15_b4&th=1"

# Creating Chrome Driver session object
option =  webdriver.ChromeOptions() 
# The Headless mode is a feature which allows the execution of a full version of the Chrome Browser
# It provides the ability to control Chrome via external programs
# The headless mode can run on servers without the need for dedicated display or graphics
option.add_argument("--headless")
# Open Chrome Driver
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=option)
# Get request to the webpage
driver.get(url)

# Here I need to select the "Most Recent" comments nasted of "Top Reviews"
# Getting the select element id
dropdown = driver.find_element(By.ID, 'cm-cr-sort-dropdown')
# Define a Select opject.. check is made that the given element is, indeed, a SELECT tag
select = Select(dropdown)
# Select the "Most Recent" option
select.select_by_value('recent')

# Parsing the html 
soup = BeautifulSoup(driver.page_source, 'lxml')
# Quit from all the browser windows and terminates the WebDriver session
driver.quit()

title = soup.select_one('#productTitle').text.strip() 

stars = soup.find('span', {'data-hook': "rating-out-of-text", 'class': "a-size-medium a-color-base"}).text.rstrip('out of 5')

reviews = soup.find_all('div', {'data-hook': "review-collapsed"})
sample_reviews = [review.text.strip() for review in reviews]

# Saving Reviews as csv file
data = pd.DataFrame({'Reviews': sample_reviews})
data.to_csv('amazon_reviews.csv', index=False)


# :shopping: Amazon Reviews Web Scraping
This a small task that I tried to challenge myself at the beginning of learning web scraping and after watching selenium tutorial on youtube. By scraping a **single product reveiws**.  
There was a problem facing me; I tried to select the "Most Recent" comments nasted of "Top Reviews"  
Then I found `selenium.webdriver.support.select` module that help me 
```python
# Getting the select element id
dropdown = driver.find_element(By.ID, 'cm-cr-sort-dropdown')
# Define a Select opject.. check is made that the given element is, indeed, a SELECT tag
select = Select(dropdown)
# Select the "Most Recent" option
select.select_by_value('recent')
```

### :book: Rreference
- [Selenium tutorial](https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ)
- [Select module](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
driver = webdriver.Edge()
driver.get(website)

# 查找ID元素
all_matches_button = driver.find_element(by=By.XPATH, value='//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(by=By.ID, value='country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)

# 获取表格内容
matches = driver.find_elements(by=By.TAG_NAME, value='tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(by=By.XPATH, value='./td[1]').text)
    home_team.append(match.find_element(by=By.XPATH, value='./td[2]').text)
    score.append(match.find_element(by=By.XPATH, value='./td[3]').text)
    away_team.append(match.find_element(by=By.XPATH, value='./td[4]').text)

df = pd.DataFrame({
    'date': date,
    'home_team': home_team,
    'score': score,
    'away_team': away_team
})

df.to_csv('football_data.csv', index=False)
# df.to_excel('football_data.xlsx', index=False)
print(df)
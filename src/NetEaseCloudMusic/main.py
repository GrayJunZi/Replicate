from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website = 'https://music.163.com/#/discover/toplist'
driver = webdriver.Edge()
driver.get(website)

iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "g_iframe")))
driver.switch_to.frame(iframe)

tr = driver.find_elements(By.XPATH, '//table[@class="m-table m-table-rank"]/tbody/tr')

for song in tr:
    td = song.find_elements(By.TAG_NAME, "td")
    rank = td[0].text
    title = td[1].find_element(By.TAG_NAME, 'b').text
    artist = td[2].text

driver.quit()
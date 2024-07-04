from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import pandas as pd

# 激活无头模式（隐藏浏览器）
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('window-size=1920x1080')

web = "https://www.audible.com/search"
driver = webdriver.Edge(options=options)
driver.get(web)
# driver.maximize_window()

container = driver.find_element(by=By.CLASS_NAME, value="adbl-impression-container ")
products = container.find_elements(by=By.XPATH, value='./div/span[2]/ul/li')

book_title = []
book_author = []
book_length = []

for product in products:
    book_title.append(product.find_element(by=By.XPATH, value='.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element(by=By.XPATH, value='.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element(by=By.XPATH, value='.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()

df_books = pd.DataFrame({
    'Title': book_title,
    'Author': book_author,
    'Length': book_length
})

df_books.to_csv('book.csv', index=False)
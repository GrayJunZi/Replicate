from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import pandas as pd

# 激活无头模式（隐藏浏览器）
options = Options()

headless = False

if headless:
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('window-size=1920x1080')

web = "https://www.audible.com/search"
driver = webdriver.Edge(options=options)
driver.get(web)

if headless is False:
    driver.maximize_window()

# 分页
pagination = driver.find_element(by=By.XPATH, value='//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(by=By.TAG_NAME, value='li')

last_page = int(pages[-2].text)

current_page = 1
book_length = []
book_title = []
book_author = []
while current_page <= last_page:
    # time.sleep(5)
    # container = driver.find_element(by=By.CLASS_NAME, value="adbl-impression-container ")
    # products = container.find_elements(by=By.XPATH, value='./div/span[2]/ul/li')
    container = WebDriverWait(driver=driver,timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME,'adbl-impression-container ')))
    products = WebDriverWait(driver=container, timeout=5).until(EC.presence_of_all_elements_located((By.XPATH, './div/span[2]/ul/li')))

    for product in products:
        book_title.append(product.find_element(by=By.XPATH, value='.//h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element(by=By.XPATH, value='.//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(by=By.XPATH, value='.//li[contains(@class, "runtimeLabel")]').text)

    current_page += 1

    try:
        next_page = driver.find_element(by=By.XPATH, value='//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

df_books = pd.DataFrame({
    'Title': book_title,
    'Author': book_author,
    'Length': book_length
})

df_books.to_csv('book.csv', index=False)
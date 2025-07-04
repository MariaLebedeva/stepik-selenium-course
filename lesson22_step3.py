from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "https://suninjuly.github.io/selects1.html"
try:
	browser = webdriver.Chrome()
	browser.get(link)

	num1 = int(browser.find_element(By.ID, "num1").text)
	num2 = int(browser.find_element(By.ID, "num2").text)


	select = Select(browser.find_element(By.TAG_NAME, "select"))
	select.select_by_visible_text(str(num1+num2))

	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка
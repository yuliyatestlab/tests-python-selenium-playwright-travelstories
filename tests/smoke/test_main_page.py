from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_main_page_loads():
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://yuliyatestlab.pythonanywhere.com"
    driver.get(url)

    # Wait page loading
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    assert driver.title != "", "Page not load"

    driver.quit()

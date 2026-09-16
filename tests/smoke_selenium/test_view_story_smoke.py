import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_view_story_page_load():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    #  1. Open the home page
    driver.get("https://yuliyatestlab.pythonanywhere.com")
    # 2.  Smoke: home page loads
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    #  3. Find first story link
    first_story = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/story')]"))
    )
    #  4. Click story link
    driver.execute_script("arguments[0].click();", first_story)

    #  5.  Smoke: story page loads without errors
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    assert driver.title != ""

    driver.quit()
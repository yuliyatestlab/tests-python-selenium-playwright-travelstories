from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout_smoke():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    #  Login
    driver.get("https://yuliyatestlab.pythonanywhere.com/login")

    email_input = wait.until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("test@test.com")
    password_input.send_keys("test123")

    login_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", login_button)

    #  Smoke: logout button exists
    logout_button = wait.until(
        EC.presence_of_element_located((By.ID, "logout"))
    )
    #  Smoke: logout button is clickable
    driver.execute_script("arguments[0].click();", logout_button)

    #  Smoke: page did not crash
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    assert driver.title != ""

    driver.quit()
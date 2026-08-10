from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_smoke():
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://yuliyatestlab.pythonanywhere.com/login"
    driver.get(url)

    wait = WebDriverWait(driver, 15)

    #  Login field
    email_input = wait.until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    password_input = driver.find_element(By.ID, "password")

    #  Enter test data
    email_input .send_keys("test@test.com")
    password_input.send_keys("test123")

    #  Login button
    login_button = driver.find_element(By.ID, "submit")

    #  Scroll the page
    driver.execute_script("arguments[0].click();", login_button)

    #  The page shouldn't crash. Any element should appear after logging in.
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    assert driver.title != ""

    driver.quit()
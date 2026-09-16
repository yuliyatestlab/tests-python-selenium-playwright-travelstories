from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration_page_load_smoke():
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://yuliyatestlab.pythonanywhere.com/register"
    driver.get(url)

    wait = WebDriverWait(driver, 15)

    #  The registration fields exist
    email_input = wait.until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    password_input = driver.find_element(By.ID, "password")
    name_input = driver.find_element(By.ID, "name")

    assert email_input.is_displayed()
    assert password_input.is_displayed()
    assert name_input.is_displayed()

    signup_button = driver.find_element(By.ID, "submit")
    #  Check that the button is clickable
    driver.execute_script("arguments[0].click();", signup_button)

    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    assert driver.title != ""

    driver.quit()
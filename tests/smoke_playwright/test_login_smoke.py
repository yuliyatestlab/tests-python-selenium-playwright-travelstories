from playwright.sync_api import Page, expect

def test_login_smoke(page: Page):
    page.goto("https://yuliyatestlab.pythonanywhere.com/login")
    # Check login form is visible
    expect(page.locator("#email")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#submit")).to_be_visible()

    # Insert test data
    page.fill("#email", "test@test.com")
    page.fill("#password", "test123")
    page.click("#submit")

    #  Check successful redirect
    expect(page).to_have_url("https://yuliyatestlab.pythonanywhere.com/")
    expect(page.locator("#logout")).to_be_visible()
from playwright.sync_api import Page, expect

def test_logout_smoke(page: Page):
    page.goto("https://yuliyatestlab.pythonanywhere.com/login")
    page.fill("#email", "test@test.com")
    page.fill("#password", "test123")
    page.click("#submit")

    # Logout
    page.click("#logout")

    #  Check successful redirect
    expect(page).to_have_url("https://yuliyatestlab.pythonanywhere.com/")
    expect(page.locator("#login")).to_be_visible()
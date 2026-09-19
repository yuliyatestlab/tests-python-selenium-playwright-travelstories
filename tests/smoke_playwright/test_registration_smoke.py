from playwright.sync_api import Page, expect

def test_registration_smoke(page: Page):
    page.goto("https://yuliyatestlab.pythonanywhere.com/register")
    #  Check registration form is visible
    expect(page.locator("#email")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#name")).to_be_visible()
    expect(page.get_by_role("button", name="Profile Image")).to_be_visible()


    #  Insert test data
    page.fill("#email", "test1@gmail.com")
    page.fill("#password", "test1234")
    page.fill("#name", "Mary")
    page.click("#submit")

    #  Check successful redirect
    expect(page).to_have_url("https://yuliyatestlab.pythonanywhere.com/login")
    expect(page.locator("#login")).to_be_visible()

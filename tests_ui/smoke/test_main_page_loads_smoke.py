from playwright.sync_api import Page, expect

def test_main_page_loads(page: Page):
    page.goto("https://yuliyatestlab.pythonanywhere.com")
    expect(page).to_have_title("Travel Stories")
    expect(page.locator("header")).to_be_visible()
    #  Checks that at list one story is visible
    expect(page.locator("h2").first).to_be_visible()
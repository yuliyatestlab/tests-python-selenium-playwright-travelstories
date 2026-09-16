from playwright.sync_api import Page, expect

def test_login_page_loads_smoke(page):
    page.goto("https://example.com")
    assert "Travel" in page.title()
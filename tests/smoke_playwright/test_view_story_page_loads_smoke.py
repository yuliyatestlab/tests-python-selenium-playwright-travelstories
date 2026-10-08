from playwright.sync_api import Page, expect

def test_view_story_page_loads(page: Page):
    page.goto("https://yuliyatestlab.pythonanywhere.com")
    first_story = (page.locator(".post-preview a")).first
    expect(first_story).to_be_visible()
    first_story.click()

    expect(page.locator(".post-heading")).to_be_visible()
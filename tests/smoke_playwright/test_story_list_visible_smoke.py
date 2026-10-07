from playwright.sync_api import Page, expect

def test_story_list_visible(page: Page):
    page.goto("https://yuliyatestlab.pythonanywhere.com")

    story_list = page.locator(".post-preview")

    expect(story_list.first).to_be_visible()
    assert story_list.count() > 0, "No stories are displayed"


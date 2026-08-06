def test_ui_smoke(page):
    page.goto("https://example.com")
    assert "Travel" in page.title()
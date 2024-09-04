from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser= playwright.chromium.launch(headless=False, slow_mo=500)
    page=browser.new_page()
    page.goto("https://katalon-demo-cura.herokuapp.com/profile.php#login")

    browser.close()
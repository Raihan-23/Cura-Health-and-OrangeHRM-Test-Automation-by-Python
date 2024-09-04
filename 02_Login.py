from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser= playwright.chromium.launch(headless=False, slow_mo=500)
    page=browser.new_page()
    page.goto("https://katalon-demo-cura.herokuapp.com/profile.php#login", wait_until='load')

    
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("John Doe")

    page.get_by_label("Password").click()
    # page.get_by_label("Password").fill("ThisIsNotAPassword")
    page.get_by_label("Password").type("ThisIsNotAPassword", delay=20)

    page.get_by_role("button", name="Login").click()


    page.get_by_label("Facility").select_option("Hongkong CURA Healthcare Center")

    page.get_by_label("Apply for hospital readmission").check()   
    page.get_by_label("Medicaid").check()

    # page.get_by_placeholder("dd/mm/yyyy").click()
    # page.get_by_placeholder("dd/mm/yyyy").fill("23/02/1998")
    page.locator("span").click()
    # page.get_by_role("cell",name='2024').click()

    # page.get_by_text("1998").click()
    # page.get_by_text("Feb").click()
    page.get_by_role("cell", name="23").click()

    page.get_by_placeholder("Comment").click()
    page.get_by_placeholder("Comment").fill("good")

    page.get_by_role("button", name="Book Appointment").click()

    page.get_by_role("link", name="Go to Homepage").click()

    page.get_by_role("link", name="").click()
    page.get_by_role("link", name="History").click()

    panel_info = page.query_selector("div.panel.panel-info").text_content()
    print(panel_info)
    # page.get_by_text("fs").highlight
    browser.close()
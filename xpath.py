from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser= playwright.chromium.launch(headless=False, slow_mo=500)
    page=browser.new_page()
    page.goto("https://katalon-demo-cura.herokuapp.com/", wait_until='load')
    page.click("//a[text()='Make Appointment']")
#login
    page.click("//label[text()='Username']")
    page.fill("//label[text()='Username']", "John Doe")

    page.click("//input[@type='password']")
    page.fill("//input[@type='password']", "ThisIsNotAPassword")

    page.click("//button[contains(@class,'btn btn-default')]")
#page2
   #dropdown
    page.locator("//select[@id='combo_facility']").select_option("Hongkong CURA Healthcare Center")

    #checkbox
    page.locator("//input[@type='checkbox' and @id='chk_hospotal_readmission']").check()

    #radio
    page.locator("//input[@type='radio' and @value='Medicaid']").click()
    #date
    page.locator("//input[@id='txt_visit_date']").click()
    page.click("//td[text()='30']")
    #comment
    page.fill("//textarea[@class='form-control']", "My appointment.")
    page.click("//button[@type='submit']")

    page.click("//i[@class='fa fa-bars']")
    page.click("//a[@href='history.php#history']")
    appointment=page.locator("//div[@class='panel panel-info']").text_content()
    print(appointment)

    browser.close()
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    
    # Go to the website
    page.goto("https://katalon-demo-cura.herokuapp.com/", wait_until='load')
    
    # Click "Make Appointment"
    page.click("//a[text()='Make Appointment']")
    
    # Wait for the login form to appear
    page.wait_for_selector("//input[@id='txt-username']")
    
    # Login
    page.fill("//input[@id='txt-username']", "John Doe")
    page.fill("//input[@id='txt-password']", "ThisIsNotAPassword")
    page.click("//button[contains(@class,'btn btn-default')]")
    
    # Verify login was successful by waiting for the appointment page to load
    page.wait_for_selector("//h2[contains(text(), 'Make Appointment')]")
    assert "appointment" in page.url, "Failed to login or incorrect page URL"
    
    # Fill in appointment details
    page.wait_for_selector("//select[@id='combo_facility']")
    page.locator("//select[@id='combo_facility']").select_option("Hongkong CURA Healthcare Center")
    
    page.wait_for_selector("//input[@id='chk_hospotal_readmission']")
    page.locator("//input[@id='chk_hospotal_readmission']").check()
    
    page.wait_for_selector("//input[@value='Medicaid']")
    page.locator("//input[@value='Medicaid']").click()
    
    # Select date
    page.wait_for_selector("//input[@id='txt_visit_date']")
    page.locator("//input[@id='txt_visit_date']").click()
    page.click("//td[text()='30']")
    
    # Add comment
    page.wait_for_selector("//textarea[@id='txt_comment']")
    page.fill("//textarea[@id='txt_comment']", "My appointment.")
    
    # Submit the appointment
    page.wait_for_selector("//button[@id='btn-book-appointment']")
    page.click("//button[@id='btn-book-appointment']")
    
    # Verify appointment confirmation
    page.wait_for_selector("//h2[contains(text(),'Appointment Confirmation')]")
    confirmation_message = page.locator("//h2[contains(text(),'Appointment Confirmation')]").text_content()
    assert "Appointment Confirmation" in confirmation_message, "Appointment confirmation failed"
    
    # Print appointment details
    appointment = page.locator("//div[@class='panel panel-info']").text_content()
    print(appointment)
    
    # Check appointment history
    page.click("//i[@class='fa fa-bars']")
    page.click("//a[@href='history.php#history']")
    
    # Wait for appointment history and print
    page.wait_for_selector("//div[@class='panel panel-info']")
    appointment_history = page.locator("//div[@class='panel panel-info']").text_content()
    print(appointment_history)
    
    browser.close()

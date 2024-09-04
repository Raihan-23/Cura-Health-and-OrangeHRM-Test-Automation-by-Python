from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # Navigate to the OrangeHRM website
    page.goto("https://www.orangehrm.com/", wait_until='load')

    # #click on the burger button
    # page.click("//span[@class='navbar-toggler-icon']")
    # Click on the 'Book a Free Demo' button using XPath
    # page.click("//a[@class='btn btn-ohrm btn-contact-sales')]")
    # page.get_by_text("Book a Free Demo").click()
    page.wait_for_selector("//a[contains(text(), 'Book a Free Demo')]", state='visible').click()

    # Wait for the form to load using XPath
    page.wait_for_selector("//form[@id='contact-form']")

    # Fill out the demo request form using XPath
    page.fill("//input[@name='firstname']", "John")
    page.fill("//input[@name='lastname']", "Doe")
    page.fill("//input[@name='company']", "ABC Corporation")
    page.fill("//input[@name='numemployees']", "100")
    page.fill("//input[@name='email']", "johndoe@example.com")
    page.fill("//input[@name='phone']", "+1234567890")
    page.select_option("//select[@name='country']", "United States")
    page.fill("//textarea[@name='message']", "I am interested in a demo of your product.")

    # Submit the form using XPath
    page.click("//button[@type='submit']")

    # Wait for the confirmation message using XPath
    page.wait_for_selector("//div[contains(@class, 'thank-you')]", timeout=10000)  # Adjust timeout as needed

    # Assert the presence of the confirmation message
    assert page.is_visible("//div[contains(@class, 'thank-you')]", timeout=10000), "Confirmation message not found"

    # Print the confirmation message
    confirmation_message = page.text_content("//div[contains(@class, 'thank-you')]")
    print(confirmation_message)

    # Additional assertion (if needed)
    assert "Thank you" in confirmation_message, "Expected text not found in the confirmation message"

    browser.close()

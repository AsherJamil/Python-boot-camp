from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

# Account details
ACCOUNT_EMAIL = 'Enter your email address'
ACCOUNT_PASSWORD = 'Enter your password'
PHONE = 'YOUR_PHONE_NUMBER'

# Function to abort application if it becomes complex or fails


def abort_application(driver):
    # Click Close Button
    try:
        close_button = driver.find_element(
            By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)
        # Click Discard Button
        discard_button = driver.find_elements(
            By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
        discard_button.click()
    except NoSuchElementException:
        print("Abort failed, elements not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Set up ChromeDriver path
chrome_driver_path = ChromeDriverManager().install()

# Set Chrome options to keep the browser open on crash
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver with the service
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to LinkedIn job search page
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3888272646&"
           "keywords=python&location=Lahore%2C%20Punjab%2C%20Pakistan")

# Reject cookies if prompted
time.sleep(2)
try:
    reject_button = driver.find_element(
        By.CSS_SELECTOR, 'button[action-type="DENY"]')
    reject_button.click()
except NoSuchElementException:
    print("No cookies rejection button found.")

# Click the sign-in button
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

# Enter login credentials and sign in
time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Wait for manual CAPTCHA solving
input("Press Enter when you have solved the CAPTCHA")

# Get all job listings on the page
time.sleep(5)
all_listings = driver.find_elements(
    By.CSS_SELECTOR, ".job-card-container--clickable")

# Loop through each job listing and apply
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply button
        apply_button = driver.find_element(
            By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        # Insert phone number if required
        time.sleep(5)
        try:
            phone_field = driver.find_element(
                By.CSS_SELECTOR, "input[id*=phoneNumber]")
            if phone_field.get_attribute("value") == "":
                phone_field.send_keys(PHONE)
        except NoSuchElementException:
            print("Phone number input not found")

        # Check if the application can be submitted directly
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application(driver)
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Close the modal
        close_button = driver.find_element(
            By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application(driver)
        print("No application button, skipped.")
        continue

# Close the browser after completing the applications
time.sleep(5)
driver.quit()

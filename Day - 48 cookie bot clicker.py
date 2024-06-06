from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import time

# Path to your ChromeDriver
chrome_driver_path = binary_path

# Set up Chrome service
service = Service(chrome_driver_path)

# Initialize the Chrome driver with the service
driver = webdriver.Chrome(service=service)

# Navigate to Cookie Clicker
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the page to load
time.sleep(5)

# Select the language (if needed)
driver.find_element(By.ID, "langSelect-EN").click()

# Wait for the game to initialize
time.sleep(5)

# Get the cookie to click on
cookie = driver.find_element(By.ID, "bigCookie")

# Get upgrade item IDs
items = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.locked)")
item_ids = [item.get_attribute("id") for item in items]

# Set initial timeout and end time for 5 minutes
timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Convert <b> text into an integer price
        for price in all_prices:
            element_text = price.text
            if element_text:
                try:
                    cost = int(element_text.split("-")
                               [1].strip().replace(",", ""))
                    item_prices.append(cost)
                except ValueError:
                    # Ignore any b elements that do not contain valid prices
                    continue

        # Create a dictionary of store items and prices
        cookie_upgrades = {item_prices[n]: item_ids[n]
                           for n in range(len(item_prices))}

        # Get current cookie count
        money_element = driver.find_element(By.ID, "cookies").text.split()[0]
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {
            cost: id for cost, id in cookie_upgrades.items() if cookie_count > cost}

        if affordable_upgrades:
            # Purchase the most expensive affordable upgrade
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes, stop the bot and check the cookies per second count
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(f"Cookies per second: {cookie_per_s}")
        break

# Close the browser
driver.quit()

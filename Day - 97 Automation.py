from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import shutil
import time
import schedule
from chromedriver_py import binary_path

CHROME_DRIVER_PATH = binary_path


def organize_downloads():
    downloads_path = os.path.expanduser("~/Downloads")

    # Define file types and their corresponding folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.wmv'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z']
    }

    # Create folders if they don't exist
    for folder in file_types:
        folder_path = os.path.join(downloads_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to appropriate folders
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(
                        downloads_path, folder, filename))
                    print(f"Moved {filename} to {folder}")
                    break


def renew_library_books():
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed and in PATH
    try:
        # Navigate to library website (replace with actual URL)
        driver.get("CHROME_DRIVER_PATH")

        # Login (you'll need to replace these with actual element IDs or XPaths)
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.send_keys("your_username")
        password.send_keys("your_password")
        driver.find_element(By.ID, "login-button").click()

        # Wait for the loans page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loans-table"))
        )

        # Find and click all 'Renew' buttons
        renew_buttons = driver.find_elements(
            By.XPATH, "//button[contains(text(), 'Renew')]")
        for button in renew_buttons:
            button.click()
            # Wait a bit between clicks to avoid overwhelming the server
            time.sleep(1)

        print("All available books renewed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


# Schedule tasks
schedule.every().day.at("09:00").do(organize_downloads)
schedule.every().monday.at("10:00").do(renew_library_books)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

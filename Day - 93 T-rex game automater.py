import time
import pyautogui
from PIL import Image


def capture_screen():
    # Capture the game area (adjust coordinates as needed)
    screenshot = pyautogui.screenshot(region=(0, 0, 1000, 300))
    return screenshot


def detect_obstacle(image):
    # Convert the image to grayscale
    gray = image.convert('L')

    # Define the area to check for obstacles
    obstacle_area = gray.crop((100, 150, 200, 200))

    # Check if there are any dark pixels (obstacles) in the area
    return any(pixel < 100 for pixel in obstacle_area.getdata())


def play_game():
    while True:
        screen = capture_screen()
        if detect_obstacle(screen):
            pyautogui.press('space')
        time.sleep(0.01)  # Small delay to prevent excessive CPU usage


if __name__ == "__main__":
    # Give the user some time to switch to the game window
    print("Switch to the game window. Starting in 5 seconds...")
    time.sleep(5)
    play_game()

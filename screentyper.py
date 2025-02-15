import time
import random
import pytesseract
from PIL import ImageGrab
import pyautogui
from pynput import keyboard

# Configure Tesseract path (if needed)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Typing speed range (40-54 WPM = 3.33 to 4.5 characters per second)
BASE_CHARS_PER_SECOND = (3.33, 4.5)

# Function to get dynamic speed
def get_dynamic_speed(char, prev_char):
    # Slow down after punctuation and at the start of a sentence
    if prev_char in ".!?":
        return random.uniform(2.8, 3.5)  # Slightly slower after punctuation
    # Speed up in the middle of words
    elif char.isalpha():
        return random.uniform(4, 4.5)  # Faster in longer words
    # Default speed range
    return random.uniform(*BASE_CHARS_PER_SECOND)

# Capture the screen and extract text
def capture_and_extract_text():
    screenshot = ImageGrab.grab()
    text = pytesseract.image_to_string(screenshot)
    paragraphs = [para.strip() for para in text.splitlines() if len(para.strip()) > 50]  # Filter long lines as paragraphs
    return '\n'.join(paragraphs).strip()

# Type the extracted text with dynamic speed
def type_text(text):
    # Click on the browser window to focus it
    pyautogui.click()  
    words = text.split()
    if len(words) > 1:
        text_to_type = ' '.join(words[1:])  # Skip the first word
        prev_char = ''
        for char in text_to_type:
            # Adjust speed dynamically
            chars_per_second = get_dynamic_speed(char, prev_char)
            delay = random.uniform(0.15, 0.2) / chars_per_second
            
            # Simulate keypresses more naturally
            if char == ' ':
                pyautogui.press('space')
            elif char == '\n':
                pyautogui.press('enter')
            else:
                pyautogui.write(char)
            
            time.sleep(delay)
            
            # Rarely simulate a typo with a backspace
            if random.random() < 0.002:  # 0.2% chance of typo
                pyautogui.press('backspace')
                time.sleep(random.uniform(0.04, 0.08))
                pyautogui.write(char)  # Re-type the corrected character

            # Pause slightly at the end of words or after punctuation
            if char in ".,!? ":
                time.sleep(random.uniform(0.1, 0.25))

            prev_char = char

typing_active = False  # Track if typing is active

def on_press(key):
    global typing_active
    if key == keyboard.Key.shift_l:  # Start typing with L Shift
        typing_active = True
        print("L Shift pressed! Capturing and typing...")
        text = capture_and_extract_text()
        type_text(text)

def on_release(key):
    global typing_active
    if key == keyboard.Key.shift_r:  # Stop typing with R Shift
        typing_active = False
        print("R Shift pressed! Typing stopped.")
        return False  # Exit listener

if __name__ == '__main__':
    print("Press L Shift to start typing and R Shift to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Capturing screen and typing... Press Ctrl+C to stop.")

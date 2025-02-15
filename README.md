# Screen-typer-bot

Tired of manually retyping on-screen text? Meet Screen Typer Bot, the intelligent typing automation tool that captures text from your screen and types it out with human-like precision! Designed to seamlessly blend into any browser or text input field, this bot replicates natural keystrokes with dynamic speed adjustments, realistic pauses, and even occasional typos (corrected just like a real person would).
Why Choose Screen Typer Bot?

Unlike traditional auto-typers that operate at robotic, monotonous speeds, Screen Typer Bot adjusts its pace dynamically, typing at 40 to 54 words per minute with slight fluctuations to mimic natural human rhythm. It slows down after punctuation, speeds up in the middle of words, and takes brief pauses at the end of sentences. This nuanced pacing ensures the typing pattern is convincing and undetectable.
Key Features:

    Realistic Typing Speed: Types at a human-like pace (40-54 WPM), with subtle speed variations.
    Dynamic Keystrokes: Uses individual key presses (pyautogui.write() and pyautogui.press()) for authentic keystrokes.
    Smart Pausing: Brief pauses after punctuation and at the end of words, just like a human would.
    Minimal Typos: Occasional, realistic typos that are quickly corrected to maintain authenticity.
    Seamless Integration: Clicks on the browser window before typing, ensuring the text appears exactly where you want it.

How It Works:

    Capture Text: The bot takes a screenshot and extracts text using Tesseract OCR.
    Smart Typing: It then types out the extracted text with realistic keystrokes and speed variations.
    Easy Control: Simply press L Shift to start typing and R Shift to stop.

Who Is It For?

Perfect for anyone looking to automate repetitive typing tasks without drawing attention. Whether you’re transcribing notes, filling out forms, or simply tired of manual retyping, Screen Typer Bot is your go-to solution!

Press L Shift to start, and let the magic happen!

Usage :

Just clone this repository and run it with python3 screentyper.py

make sure u install the neccessary requirements give below;

pip3 install pytesseract pynput pillow pyautogui --break-system-packages





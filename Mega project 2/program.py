import pyautogui
import time
import pyperclip

# Delay to switch to the required window
time.sleep(3)

# Click on the icon at (1137, 1054)
pyautogui.click(1137, 1054)
time.sleep(1)  # Small delay for UI response

# Click and drag from (895, 189) to (1412, 728) to select text
pyautogui.moveTo(895, 189)
pyautogui.mouseDown()
pyautogui.moveTo(1412, 728, duration=0.5)
pyautogui.mouseUp()
time.sleep(0.5)  # Allow time for selection

# Copy the selected text to clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Give time for copying

# Retrieve copied text from clipboard
copied_text = pyperclip.paste()
print("Copied Text:", copied_text)

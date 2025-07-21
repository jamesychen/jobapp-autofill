import keyboard
import pyautogui
import pyperclip
import time
import json
import os

# === Load data ===
with open("data/autofill.json", "r", encoding="utf-8") as f:
    autofill = json.load(f)

# === Paste function ===
def paste_value(key):
    value = autofill.get(key)
    if value:
        pyautogui.press('backspace')
        pyperclip.copy(value)
        time.sleep(0.05)
        pyautogui.hotkey("ctrl", "v")
        print(f"✅ Pasted for key [{key}]")
    else:
        print(f"❌ No value mapped for key [{key}].")

# === Register hotkeys ===
for k in autofill:
    keyboard.add_hotkey(k, lambda k=k: paste_value(k), suppress=False)

print("💡 Ready! Type a single key (e.g. 'f', '1', etc.) to autofill. Backspace will clear the key.")
keyboard.wait()

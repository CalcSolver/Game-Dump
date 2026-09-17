import ctypes
import os
import random
import time
import tkinter as tk

# Play Windows error sound
def error_sound():
    ctypes.windll.user32.MessageBeep(0x00000010)

# Spam error popups (safe)
def spam_errors():
    for _ in range(50):
        error_sound()
        ctypes.windll.user32.MessageBoxW(
            None,
            "Critical System Fault\nMemory integrity compromised.",
            "Windows Error",
            0x10
        )

# Fake BSOD fullscreen window
def fake_bsod():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="#0000AA")  # classic BSOD blue

    label = tk.Label(
        root,
        text=(
            "A problem has been detected and Windows has been shut down to prevent damage.\n\n"
            "KERNEL_SECURITY_CHECK_FAILURE\n\n"
            "If this is the first time you've seen this Stop error screen,\n"
            "restart your computer. If this screen appears again, follow\n"
            "these steps:\n\n"
            "Check for viruses on your computer.\n"
            "Remove any newly installed hard drives or hard drive controllers.\n"
            "Check your hard drive to make sure it is properly configured.\n\n"
            "*** STOP: 0x000000139"
        ),
        fg="white",
        bg="#0000AA",
        font=("Consolas", 20)
    )
    label.pack(expand=True)

    root.mainloop()

# Light memory spam (safe)
junk = []
def eat_memory():
    for _ in range(200):
        junk.append("X" * random.randint(50000, 150000))
        time.sleep(0.02)

# Run everything
spam_errors()
eat_memory()
fake_bsod()

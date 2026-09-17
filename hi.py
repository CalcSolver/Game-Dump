import tkinter as tk
import random
import threading
import time
import pygame

# Load MP3 sound
pygame.mixer.init()
pygame.mixer.music.load("erro.mp3")  # download the MP3 into same folder

windows = []

def spawn_error_window():
    win = tk.Tk()
    win.title("Windows Error")
    win.geometry("300x120")

    # Random diagonal glitch positions
    x = random.randint(0, win.winfo_screenwidth() - 300)
    y = random.randint(0, win.winfo_screenheight() - 120)
    win.geometry(f"+{x}+{y}")

    label = tk.Label(win, text="Critical System Fault\nMemory integrity compromised.", fg="red")
    label.pack(expand=True)

    windows.append(win)

    # Play sound
    pygame.mixer.music.play()

    win.after(2000, lambda: None)  # keep window alive
    win.mainloop()

def spam_windows():
    for _ in range(50):
        threading.Thread(target=spawn_error_window, daemon=True).start()
        time.sleep(0.05)

def fake_bsod():
    bsod = tk.Tk()
    bsod.attributes("-fullscreen", True)
    bsod.configure(bg="#0000AA")

    text = (
        "A problem has been detected and Windows has been shut down to prevent damage.\n\n"
        "KERNEL_SECURITY_CHECK_FAILURE\n\n"
        "If this is the first time you've seen this Stop error screen,\n"
        "restart your computer. If this screen appears again, follow\n"
        "these steps:\n\n"
        "Check for viruses on your computer.\n"
        "Remove any newly installed hard drives or controllers.\n"
        "Check your hard drive configuration.\n\n"
        "*** STOP: 0x000000139\n\n"
    )

    label = tk.Label(bsod, text=text, fg="white", bg="#0000AA", font=("Consolas", 20))
    label.pack(expand=True)

    def fix_everything():
        for w in windows:
            try:
                w.destroy()
            except:
                pass
        bsod.destroy()

    btn = tk.Button(bsod, text="Report to Windows", font=("Consolas", 18), command=fix_everything)
    btn.pack()

    bsod.mainloop()

# Run chaos
threading.Thread(target=spam_windows, daemon=True).start()
time.sleep(5)
fake_bsod()

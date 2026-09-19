import tkinter as tk
import random
import subprocess
import sys
import os

root = tk.Tk()
root.title("System Cleaner")
root.geometry("800x500")
root.configure(bg="black")

title = tk.Label(
    root,
    text="Deleting files...",
    font=("Consolas", 24),
    fg="white",
    bg="black"
)
title.pack(pady=30)

status = tk.Label(
    root,
    text="Starting...",
    font=("Consolas", 16),
    fg="white",
    bg="black"
)
status.pack(pady=10)

progress = tk.Label(
    root,
    text="0%",
    font=("Consolas", 20),
    fg="white",
    bg="black"
)
progress.pack(pady=10)

percent = 0


def finish_program():
    status.config(text="Finished deleting.")
    progress.config(text="100%")

    # Launch the fake BSOD
    bsod_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "B.py")
    subprocess.Popen([sys.executable, bsod_path])


def update_progress():
    global percent

    if percent < 100:
        percent += random.randint(1, 5)

        if percent > 100:
            percent = 100

        progress.config(text=f"{percent}%")

        root.after(
            random.randint(80, 200),
            update_progress
        )
    else:
        root.after(1000, finish_program)


update_progress()

root.mainloop()
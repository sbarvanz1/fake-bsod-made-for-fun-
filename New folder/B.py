import tkinter as tk
import random

root = tk.Tk()
root.title("Windows")
root.attributes("-fullscreen", True)
root.configure(bg="#0078D7")

# Hide the mouse cursor
root.config(cursor="none")


def close_bsod(event=None):
    # Restore the cursor before closing
    root.config(cursor="")
    root.destroy()


root.bind("<Escape>", close_bsod)

# Main BSOD text
sad_face = tk.Label(
    root,
    text=":(",
    font=("Segoe UI", 72),
    fg="white",
    bg="#0078D7"
)
sad_face.place(x=100, y=70)

message = tk.Label(
    root,
    text="Your PC ran into a problem and needs to restart.\n"
         "We're just collecting some error info, and then we'll restart for you.",
    font=("Segoe UI", 22),
    fg="white",
    bg="#0078D7",
    justify="left"
)
message.place(x=105, y=220)

# Fake progress
progress = tk.Label(
    root,
    text="0% complete",
    font=("Segoe UI", 20),
    fg="white",
    bg="#0078D7"
)
progress.place(x=105, y=305)

# Fake URL
url = tk.Label(
    root,
    text="For more information about this issue, visit:\n"
         "https://windows.example.invalid/help",
    font=("Segoe UI", 16),
    fg="white",
    bg="#0078D7",
    justify="left"
)
url.place(x=105, y=350)

# Fake stop code
stop_code = tk.Label(
    root,
    text="Stop code: CRITICAL_PROCESS_DIED",
    font=("Segoe UI", 16),
    fg="white",
    bg="#0078D7"
)
stop_code.place(x=105, y=440)


# Make a QR-like graphic
qr_size = 29
cell_size = 4

canvas = tk.Canvas(
    root,
    width=qr_size * cell_size,
    height=qr_size * cell_size,
    bg="white",
    highlightthickness=0
)
canvas.place(x=105, y=500)


def draw_finder(x, y):
    # Outer square
    canvas.create_rectangle(
        x, y,
        x + 7 * cell_size,
        y + 7 * cell_size,
        fill="black",
        outline=""
    )

    # White middle
    canvas.create_rectangle(
        x + cell_size,
        y + cell_size,
        x + 6 * cell_size,
        y + 6 * cell_size,
        fill="white",
        outline=""
    )

    # Black center
    canvas.create_rectangle(
        x + 2 * cell_size,
        y + 2 * cell_size,
        x + 5 * cell_size,
        y + 5 * cell_size,
        fill="black",
        outline=""
    )


# Three QR finder patterns
draw_finder(0, 0)
draw_finder((qr_size - 7) * cell_size, 0)
draw_finder(0, (qr_size - 7) * cell_size)


# Random-looking QR data
random.seed(12345)

for row in range(qr_size):
    for col in range(qr_size):

        # Leave space for finder patterns
        if (
            (row < 8 and col < 8) or
            (row < 8 and col >= qr_size - 8) or
            (row >= qr_size - 8 and col < 8)
        ):
            continue

        if random.randint(0, 1):
            canvas.create_rectangle(
                col * cell_size,
                row * cell_size,
                (col + 1) * cell_size,
                (row + 1) * cell_size,
                fill="black",
                outline=""
            )


# Fake progress animation
percent = 0


def update_progress():
    global percent

    if percent < 100:
        percent += random.randint(1, 4)

        if percent > 100:
            percent = 100

        progress.config(text=f"{percent}% complete")

        root.after(
            random.randint(80, 250),
            update_progress
        )


update_progress()

root.mainloop()
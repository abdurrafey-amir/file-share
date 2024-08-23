
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\abdur\OneDrive\Desktop\file-share\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("656x651")
window.configure(bg = "#142F44")


canvas = Canvas(
    window,
    bg = "#142F44",
    height = 651,
    width = 656,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    656.0,
    651.0,
    fill="#142F44",
    outline="")

canvas.create_text(
    178.0,
    146.0,
    anchor="nw",
    text="File Share",
    fill="#F6683B",
    font=("Inter Bold", 64 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    328.0,
    361.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F6683B",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=112.0,
    y=325.0,
    width=432.0,
    height=70.0
)

canvas.create_text(
    251.0,
    343.0,
    anchor="nw",
    text="File name",
    fill="#142F44",
    font=("Inter Bold", 30 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=224.0,
    y=540.0,
    width=209.0,
    height=64.0
)

canvas.create_rectangle(
    108.0,
    445.0,
    549.0,
    493.0,
    fill="#F6683B",
    outline="")

canvas.create_text(
    273.0,
    451.0,
    anchor="nw",
    text="Progress",
    fill="#142F44",
    font=("Inter Bold", 25 * -1)
)

canvas.create_text(
    108.0,
    502.0,
    anchor="nw",
    text="0%",
    fill="#F6683B",
    font=("Inter Bold", 25 * -1)
)

canvas.create_text(
    481.0,
    503.0,
    anchor="nw",
    text="100%",
    fill="#F6683B",
    font=("Inter Bold", 25 * -1)
)
window.resizable(False, False)
window.mainloop()

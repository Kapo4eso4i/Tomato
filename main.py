#!/usr/bin/env python
import tkinter as tk

def go_work():
    countdown(1500)

def relax():
    countdown(300)


def countdown(sec):
    mins = round(sec / 60)
    secs = sec % 60
    canvas.itemconfig(timer, text=f"{mins}:{secs}")
    if sec > 0:
        root.after(1000, countdown, sec - 1)


root = tk.Tk()
root.config(background="#ffffcc")
root.geometry("400x400")
root.title("Pomodoro")

bg_image = tk.PhotoImage(file = "tomato.png")
cherry_image = tk.PhotoImage(file="cherry.png")

canvas = tk.Canvas(root,height=360, width=360, bg="#ffffcc", highlightthickness=0)
canvas.create_image(180, 180, image=bg_image)
timer = canvas.create_text(180, 180, text="00:00", font=("Digital-7", 26, "bold", "italic"), fill="#ffff66")
canvas.create_text(180, 120, text="Timer", font=("neuropolitical", 20, "bold", "italic"), fill="#ffff66")
canvas.create_image(30, 50, image=cherry_image)
canvas.grid(row=0, column=0, rowspan=2, columnspan=2)

button1 = tk.Button(root, text="Start",width=8,bg="#cc00ff", command=go_work)
button1.grid(row=2, column=0)

button2 = tk.Button(root, text="Reset", width=8)
button2.grid(row=2, column=1)



root.mainloop()

#!/usr/bin/env python
import tkinter as tk
from playsound import playsound

WORK_TIME_MIN = 25
RELAX_TIME_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
cherry_pos = 20
my_timer = None


def job():
    global reps
    global cherry_pos
    if reps == 7:
        playsound("large-crowd-applause-sound-effect.mp3", block=False)
        reps = 0
        canvas.delete("cherry")
        cherry_pos = 20
        canvas.itemconfig(text, text="Long Break")
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2:
        relax()
        reps += 1
        cherry_pos += 70
        canvas.create_image(20, cherry_pos, image=cherry_image, tags="cherry")
    else:
        reps += 1
        go_work()


def go_work():
    playsound("horn-sound.mp3", block=False)
    canvas.itemconfig(text, text="Work!")
    countdown(WORK_TIME_MIN * 60)


def relax():
    playsound("free-music-logo-transition-sound.mp3", block=False)
    canvas.itemconfig(text, text="Relax")
    countdown(RELAX_TIME_MIN * 60)


def countdown(sec):
    global my_timer
    sec -= 1
    mins = sec // 60
    secs = sec % 60
    canvas.itemconfig(timer, text="%02d:%02d" % (mins, secs))
    if sec > 0:
        my_timer = root.after(1000, countdown, sec - 1)
    else:
        job()


def reset():
    global reps
    global cherry_pos
    global my_timer
    reps = 0
    canvas.delete("cherry")
    cherry_pos = 20
    canvas.itemconfig(text, text="Timer")
    canvas.itemconfig(timer, text="00:00")
    root.after_cancel(my_timer)


root = tk.Tk()
root.config(background="#ffffcc")
root.geometry("400x400")
root.title("Pomodoro")

bg_image = tk.PhotoImage(file="tomato.png")
cherry_image = tk.PhotoImage(file="cherry.png")

canvas = tk.Canvas(root, height=360, width=360, bg="#ffffcc", highlightthickness=0)
canvas.create_image(180, 180, image=bg_image)
timer = canvas.create_text(180, 160, text="00:00", font=("digital-7 mono", 40, "bold", "italic"), fill="#ffffff")
text = canvas.create_text(180, 220, text="Timer", font=("neuropolitical", 20, "bold", "italic"), fill="#ffffff")
# canvas.create_image(30, 50, image=cherry_image)
canvas.grid(row=0, column=0, rowspan=2, columnspan=2)

button1 = tk.Button(root, text="Start", width=8, command=job)
button1.grid(row=2, column=0)

button2 = tk.Button(root, text="Reset", width=8, command=reset)
button2.grid(row=2, column=1)


root.mainloop()

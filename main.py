from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    global REPS
    REPS = 0
    timer_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    print(REPS)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        Label.config(timer_label, text="Long Break", font=(FONT_NAME, 30, "bold"), fg=RED, bg=YELLOW)
        timer_label.grid(row=0, column=1)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        Label.config(timer_label, text="Break", font=(FONT_NAME, 30, "bold"), fg=PINK, bg=YELLOW)
        timer_label.grid(row=0, column=1)
    else:
        count_down(work_sec)
        Label.config(timer_label, text="Work", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
        timer_label.grid(row=0, column=1)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS == 2:
            tick_label.config(text="✓")
        elif REPS == 4:
            tick_label.config(text="✓✓")
        elif REPS == 6:
            tick_label.config(text="✓✓✓")
        elif REPS == 8:
            tick_label.config(text="✓✓✓✓")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

stop_button = Button(text="Stop", highlightthickness=0, command=reset)
stop_button.grid(row=2, column=2)

tick_label = Label(font=(FONT_NAME, 15, "bold"), fg=RED, bg=YELLOW)
tick_label.grid(row=3, column=1)

window.mainloop()

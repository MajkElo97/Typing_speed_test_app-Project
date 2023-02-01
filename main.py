from tkinter import *
import time

SAMPLE_TEXT = "A grasshopper spent the summer hopping about in the sun and singing to his heart's content."
NUMBER_OF_WORDS = len(SAMPLE_TEXT.split())

start_time = 0
stop_time = 0


def close_app():
    root.destroy()


def start_timer():
    global start_time, stop_time
    start_time = time.time()
    stop_time = 0
    button_start.config(bg='green', text="Reset")
    button_stop.config(bg='white')
    success_text.set("")
    text_input.delete("1.0", "end")


def stop_timer():
    global stop_time, start_time
    if start_time != 0:
        stop_time = time.time()
        button_start.config(bg='white', text="Start")
        button_stop.config(bg='red')
        time_delta = round(stop_time - start_time, 2)
        start_time = 0
        stop_time = 0
        user_text = text_input.get("1.0", "end-1c")
        user_text_len = len(user_text.split())
        cpm = round((len(user_text) / time_delta) * 60)
        if (user_text_len == NUMBER_OF_WORDS) & (user_text == SAMPLE_TEXT):
            wpc = round((user_text_len / time_delta) * 60)
            success_text.set(f"You are writing: {cpm} characters per minute [CPM]\n"
                             f"Your writing speed is: {wpc} words per minute [WPC]")
        else:
            success_text.set(
                f"Wrong text You piece of hamster!!! Try again. \nYou are writing: {cpm} characters per minute [CPM]")


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.config(padx=60, pady=60, bg="white")
root.title("Typing speed test")

start_label = Label(text="'Press start and start writing text below'", bg="white")
start_label.grid(row=0, column=0, columnspan=2)

text_label = Label(text=SAMPLE_TEXT, bg="white")
text_label.grid(row=1, column=0, columnspan=2, pady=10)

text_input = Text(width=80, height=10)
text_input.grid(row=2, columnspan=2, pady=10, column=0)

button_start = Button(text="Start", command=start_timer, width=30)
button_start.grid(row=3, column=0, pady=10)

button_stop = Button(text="Stop", command=stop_timer, width=30)
button_stop.grid(row=3, column=1, pady=10)

button_quit = Button(text="Quit", command=close_app, width=30)
button_quit.grid(row=4, column=0, columnspan=2, pady=10)

success_text = StringVar()
success_text.set("")
success_label = Label(textvariable=success_text, background='white')
success_label.grid(row=5, column=0, columnspan=2)

root.mainloop()

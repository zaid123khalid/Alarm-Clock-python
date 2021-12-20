from tkinter import *
import time
import datetime
import winsound
from threading import Thread

alarm = Tk()
alarm.title("Alarm Clock")

disp = StringVar()


def Threading():
    t1 = Thread(target=Alarm)
    t1.start()


def update():
    time_string = time.strftime("%I:%M:%S %p")
    l1.config(text=time_string)

    l1.after(1000, update)


def Alarm():
    while True:
        set_alarm_time = f"{hrs.get()}:{mins.get()}:{sec.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        a = ("alarm set for", set_alarm_time)
        disp.set(a)
        if current_time == set_alarm_time:
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


l1 = Label(alarm, font=("Free style", 50, "italic"), fg="#00FF00", bg="black")
l1.grid(row=1, column=2)
update()

hrs = Entry(alarm, font=50, bg="black", fg="white")
hrs.bind("<Button-1>", lambda e: hrs.delete(0, END))
hrs.insert(0, "Hours")
hrs.grid(row=2, column=2)

mins = Entry(alarm, font=50, bg="black", fg="white")
mins.bind("<Button-1>", lambda e: mins.delete(0, END))
mins.insert(0, "Minutes")
mins.grid(row=3, column=2)

sec = Entry(alarm, font=50, bg="black", fg="white")
sec.bind("<Button-1>", lambda e: sec.delete(0, END))
sec.insert(0, "Seconds")
sec.grid(row=4, column=2)

btn = Button(alarm, text="Set Alarm", bg="black", fg="white",width=15 ,command=Threading)
btn.grid(row=5, column=2)

l2 = Label(alarm, textvariable=disp, font=50, width=20, fg="#00FF00", bg="black")
l2.grid(row=6, column=2)

alarm.mainloop()
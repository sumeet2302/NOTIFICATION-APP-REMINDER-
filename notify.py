from tkinter import*
from tkinter import messagebox

from PIL import Image , ImageTk
from plyer import notification
import time
t=Tk()
t.title("Notification-app")
t.geometry("500x300")
img = Image.open("notify-label.png")
L_image = ImageTk.PhotoImage(img)

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All field are required")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification")
        t.destroy()
        time.sleep(min_to_sec)
        notification.notify(title="Title",
                            message="get_msg",
                            app_icon=None,
                            app_name="notifier",
                            timeout=10)

img_label = Label(t, image=L_image).grid()

t_label = Label(t, text="Title to notify", font=("poppins", 10))
t_label.place(x=12, y=70)
title = Entry(t, width="25", font=("poppins", 10))
title.place(x=123, y=78)

m_label = Label(t,text="Display message", font=("poppins", 10))
m_label.place(x=12, y=120)
msg = Entry(t, width="25", font=("poppins", 10))
msg.place(x=123, y=120, height=30)

time_label = Label(t, text="Set time", font=("poppins", 10))
time_label.place(x=12, y=175)
time1 = Entry(t, width="5", font=("poppins", 10))
time1.place(x=123, y=175)

time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.resizable(0, 0)
t.mainloop()


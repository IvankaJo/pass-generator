import random
from tkinter import messagebox
from tkinter import *


# Password function
def gen_pass():
    try:
        repeat = int(repeat_entry.get())
        lenght = int(length_entry.get())
    except:
        messagebox.showerror(message="please input keys")

    if repeat == 1:
        password = random.sample(character_string, lenght)
    else:
        password = random.choices(character_string, k=lenght)

    password = ''.join(password)
    password_v = StringVar()
    password ="Created password: " + str(password)
    password_v.set(password)

    password_label = Entry(password_gen, bd=0, bg="gray85", textvariable= password_v, state="readonly")
    password_label.place(x=10, y=140, height=50, width=320)
        
character_string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

#Define the user interface
password_gen  = Tk()
password_gen.geometry("350x200")
password_gen.title("GenPass")

#Mention the title of the app
title_label = Label(password_gen, text="Let's make nice pass-mess", font=('Ubuntu Mono',12))
title_label.pack()
#Read length
length_label = Label(password_gen, text="Enter length of password: ")
length_label.place(x=20,y=30)
length_entry = Entry(password_gen, width=3)
length_entry.place(x=190,y=30)
#Read repetition
repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise: ")
repeat_label.place(x=20,y=60)
repeat_entry = Entry(password_gen, width=3)
repeat_entry.place(x=300,y=60)

#Generate password
password_button = Button(password_gen, text="Generate Pass", command=gen_pass)
password_button.place(x=130,y=110)
#Exit and close the app
password_gen.mainloop()
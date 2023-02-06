from AppOpener import open
import webbrowser
import tkinter as tk
from tkinter import *
# open("LS")

def display():
    if(x.get()==1):
        print('walter is cool')
    else: 
        print('walter is still cool but ur cringe cuz u didnt say he is')

window = tk.Tk()
x = IntVar()
check_button = Checkbutton(window, text='Walter is cool', variable=x, onvalue=1, offvalue=0, command=display)
check_button.pack()



# var1 = tk.IntVar()

# def e():
#     global var1
#     print(var1.get())

# c1 = tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=e)
# c1.pack()






window.mainloop()

#importing tkinter libraries
import tkinter as tk
from tkinter import *
import webbrowser

def run_credits():

    #sets window size and starts it maximized
    window = tk.Tk()
    window.geometry('1920x1080')
    window.state('zoomed')
    window.configure(bg='#19a7e9')

    font1 = ('Default', 25)
    greeting = tk.Label(text='Credits', font=font1)
    greeting.place(x=700, y=25)

    #function that allows you to go home
    def go_home():
        window.destroy()
        import main
        main.main_run()
    
    #credit text
    credit_list = tk.Label(text="Thanks to the following groups: \nKhan Acadamy\nCodeacadamy\nDesmos\nMicrosoft Office\nStack Overflow\nOracle\nPython\nC#\nUnity\nHTML\nSteam\nMicrosoft/Mojang\nNinja Kiwi\nBlizzard\nEA\nRiot Games\n\nAll Companies/Corparations Have All Rights Reserved for their Products.")
    credit_list.place(x=570, y=220)

    #back button
    back_button = tk.Button(text='Home', width=10, height=3, bg='#c197ff', fg='black', command=go_home)
    back_button.place(x=25, y=720)


    window.mainloop()


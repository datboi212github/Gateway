#imports the tkinter libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def main_run():
    #creates home window and sets size
    home_window = tk.Tk()
    home_window.geometry('1920x1080')
    home_window.state('zoomed')

    home_window.configure(bg='#d99964')

    #creates greeting label + font and adds it to the screen

    font1 = ('Default', 25)
    font2 = ('Default', 15)
    credits_font = ('Default', 10)
    greeting = tk.Label(text="Welcome to Gateway", font=font1)
    greeting2 = tk.Label(text="Click a button to navigate to its screen", font=font2)
    greeting.place(x=605, y = 25)
    greeting2.place(x=590, y=75)

    credits = tk.Label(text='Created by Omkar Page and Tejas Panja - Copyright 2023', font=credits_font)
    credits.place(x=600,y=720)

    def run_homework():
        home_window.destroy()
        import homework
        homework.homework_run()

    def run_gaming():
        home_window.destroy()
        import gaming
        gaming.run_gaming()

    def run_coding():
        home_window.destroy()
        import coding
        coding.run_coding()

    def run_social():
        home_window.destroy()
        import social
        social.run_social()
        
    def run_credits():
        home_window.destroy()
        import credits
        credits.run_credits()
        
    #all of the buttons and what they do
    homework_button = tk.Button(text = 'HOMEWORK', width=30, height=5, bg='#64a4d9', fg='black',command=run_homework)
    homework_button.place(x=660, y=125)
    gaming_button = tk.Button(text = 'GAMING', width= 30, height=5, bg='#64a4d9', fg='black', command=run_gaming)
    gaming_button.place(x=660, y=275)
    coding_button = tk.Button(text = 'CODING', width= 30, height=5, bg='#64a4d9', fg='black', command=run_coding)
    coding_button.place(x=660, y=425)
    social_button = tk.Button(text = 'SOCIAL', width= 30, height=5, bg='#64a4d9', fg='black', command=run_social)
    social_button.place(x=660, y=575)
    credits_button = tk.Button(text = 'CREDITS', width= 10, height=5, bg='#64a4d9', fg='black', command=run_credits)
    credits_button.place(x=1430, y=690)

    home_window.mainloop()




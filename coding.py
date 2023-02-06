#importing tkinter libraries
import tkinter as tk
from tkinter import *

#importing coding library
import open_coding

def run_coding():

    #creating window + setting bg color
    window = tk.Tk()
    window.geometry('1920x1080')
    window.state('zoomed')
    window.configure(bg='#2700ff')

    #creating fonts + adding title and subtitles
    font1 = ("Default", 25)
    font2 = ("Default", 15)
    greeting = tk.Label(text="Welcome to the Coding Section", font=font1)
    greeting2 = tk.Label(text='Ignore quotation marks when typing in language', font=font2)
    greeting.place(x=550, y=25)
    greeting2.place(x=570, y=75)


    def run_learn():
        #opening stack overflow + learning for language
        lang = language_input.get()
        open_coding.open_stack_overflow()
        if (lang == 'py'):
            open_coding.learn_python()
        elif (lang == 'java'):
            open_coding.learn_java()
        elif (lang == 'cs'):
            open_coding.learn_csharp()
        elif (lang == 'html'):
            open_coding.learn_html()
        
    
    def run_write():
        #opening stack overflow + writing for language
        lang = language_input.get()
        open_coding.open_stack_overflow()
        if (lang == 'py'):
            open_coding.write_python()
        elif (lang == 'java'):
            open_coding.write_java()
        elif (lang == 'cs'):
            open_coding.write_csharp()
        elif (lang == 'html'):
            open_coding.write_html()
        else:
            open_coding.write_other()

    #command for back button
    def go_home():
        window.destroy()
        import main
        main.main_run()

    #language input box + text
    language_text = tk.Label(text='Enter the language you want to code or learn here')
    language_text.place(x=640, y=180)
    language_input = tk.Entry(fg='black', bg='white', width=50)
    language_input.place(x=625, y=200)

    #button to select learn
    learn_button = tk.Button(text='Learn', width=30, height=5, bg='#d8ff00', fg='black', command=run_learn)
    learn_button.place(x=850, y=500)

    #button to select write
    write_button = tk.Button(text='Write', width=30, height=5, bg='#d8ff00', fg='black', command=run_write)
    write_button.place(x=450, y=500)

    
    language_info = tk.Label(text='Languages:\nPython: "py"\nJava: "java"\nC#: "cs"\nHTML: "html"\nOther: "other"')
    language_info.place(x=725, y=300)
    
    back_button = tk.Button(text='Home', width=10, height=3, bg='#d8ff00', fg='black', command=go_home)
    back_button.place(x=25, y=720)

    window.mainloop()


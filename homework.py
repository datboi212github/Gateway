#importing tkinter libraries
import tkinter as tk
from tkinter import *
import webbrowser

#importing file libraries
import open_homework_english
import open_homework_math
import open_homework_science
import open_homework_sat
import open_homework_history

grade = ""
subject = ""

def homework_run():
    #sets window size and starts it maximized
    window = tk.Tk()
    window.geometry('1920x1080')
    window.state('zoomed')
    window.configure(bg='#d5ff97')

    #sets the font to defaut, creates greeting at the top and adds it to the screen
    font1 = ("Default", 25)
    font2 = ("Default", 15)
    greeting = tk.Label(text="Welcome to the Homework Section", font=font1)
    quotes_warning = tk.Label(text='When inputting subjects, ignore the quotation marks\nIf nothing happens, please check your inputs\nFORMAT: (grade) - "subject"', font=font2)
    greeting.place(x=535, y=25)
    quotes_warning.place(x=560, y=75)

    #grade and subject variables

    global grade
    global subject

    #defines all of the grades and the command for them
    def first_grade():
        if subject == "math":
            open_homework_math.first_grade()
            open_homework_math.open_calculator()

    def second_grade():
        if subject == 'math':
            open_homework_math.second_grade()
            open_homework_math.open_calculator()
        elif subject == 'english':
            open_homework_english.second_grade()

    def third_grade():
        if subject == 'math':
            open_homework_math.third_grade()
            open_homework_math.open_calculator()
        elif subject == 'english':
            open_homework_english.third_grade()

    def fourth_grade():
        if subject == 'math':
            open_homework_math.fourth_grade()
            open_homework_math.open_calculator()
        elif subject == 'english':
            open_homework_english.fourth_grade()

    def fifth_grade():
        if subject == 'math':
            open_homework_math.fifth_grade()
            open_homework_math.open_calculator()
        elif subject == 'english':
            open_homework_english.fifth_grade()

    def sixth_grade():
        if subject == 'math':
            open_homework_math.sixth_grade()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'english':
            open_homework_english.sixth_grade()
        elif subject == 'science':
            open_homework_science.middle_physics()

    def seventh_grade():
        if subject == 'math':
            open_homework_math.seventh_grade()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'english':
            open_homework_english.seventh_grade()
        elif subject == 'science':
            open_homework_science.middle_bio()

    def eight_grade():
        if subject == 'math':
            open_homework_math.eighth_grade()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'english':
            open_homework_english.eighth_grade()  
        elif subject == 'science':
            open_homework_science.middle_earth_and_space()      

    def ninth_grade():
        if subject == 'math':
            open_homework_math.ninth_grade()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'english':
            open_homework_english.ninth_grade()
        elif subject == 'science':
            open_homework_science.high_bio()
        elif subject == 'history':
            open_homework_history.ancient_history()

    def tenth_grade():
        if subject == 'math':
            open_homework_math.tenth_grade()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'science':
            open_homework_science.high_physics()
        elif subject == 'history':
            open_homework_history.modern_history()
            
    def eleventh_grade():
        if subject == 'math':
            open_homework_math.eleventh_grade()
            open_homework_math.open_desmos()
            open_homework_math.open_calculator() 
        elif subject == 'history':
            open_homework_history.us_history()

    def twelvth_grade():
        if subject == 'math':
            open_homework_math.twelvth_grade()
            open_homework_math.open_desmos()
            open_homework_math.open_calculator() 
        elif subject == 'history':
            open_homework_history.us_gov()

    def other_subjects():
        if subject == 'trig':
            open_homework_math.trigonometry()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'stats':
            open_homework_math.statistics()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'calcab':
            open_homework_math.calcAB()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'calcbc':
            open_homework_math.calcBC()
            open_homework_math.open_calculator()
            open_homework_math.open_desmos()
        elif subject == 'grammar':
            open_homework_english.grammar()
        elif subject == 'collegebio':
            open_homework_science.college_bio()
        elif subject == 'collegechem':
            open_homework_science.college_chem()
        elif subject == 'collegees':
            open_homework_science.college_ES()
        elif subject == 'collegephysics':
            open_homework_science.college_physics()
        elif subject == 'sat':
            open_homework_sat.sat()

    #checking which option is selected
    def get_vars():
        global grade
        global subject
        grade = grade_entry.get()
        subject = subject_entry.get()
        if(grade == "1"):
            first_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "2"):
            second_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "3"):
            third_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "4"):
            fourth_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "5"):
            fifth_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "6"):
            sixth_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "7"):
            seventh_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "8"):
            eight_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "9"):
            ninth_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "10"):
            tenth_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "11"):
            eleventh_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "12"):
            twelvth_grade()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)
        elif(grade == "other"):
            other_subjects()
            webbrowser.open('https://www.microsoft.com/en-us/microsoft-365?ms.url=office365com&rtc=1', new=2)

    def go_home():
        window.destroy()
        import main
        main.main_run()


    #inputs a button on the tkinter interface
    button = tk.Button(text='Get Study Materials', width=30, height=5, bg='#c197ff', fg='black', command=get_vars)
    button.place(x=660, y=685)

    #adds the text box and label for inputting grade
    grade_text = tk.Label(text='Input grade here')
    grade_text.place(x=625, y=220)
    grade_entry = tk.Entry(fg='black', bg = 'white', width=50)
    grade_entry.place(x=625, y=240)

    #adds the text box and label for inputting subject
    subject_text = tk.Label(text='Input subject here')
    subject_text.place(x=625, y=170)
    subject_entry = tk.Entry(fg='black', bg = 'white', width=50)
    subject_entry.place(x=625, y=190)

    #displays the command prompts for each subject and grade
    options_help = tk.Label(text='First Grade (1): Subjects - "math"\nSecond Grade (2): Subjects - "math", "english"\nThird Grade (3): Subjects - "math", "english"\nFourth Grade (4): Subjects - "math", "english"\nFifth Grade (5): Subjects - "math", "english"\nSixth Grade (6): Subjects - "math", "english", "science"\nSeventh Grade (7): Subjects - "math", "english", "science"\nEighth Grade (8): Subjects - "math", "english", "science"\nNinth Grade (9): Subjects - "math", "english", "science", "history"\nTenth Grade (10): Subjects - "math", "science", "history"\nEleventh Grade (11): Subjects - "math", "history"\n Twelvth Grade (12): Subjects - "math", "history"\n\nOther Subjects (other):\n\nTrigonometry - "trig"\nStatistics - "stats"\nCalculus AB - "calcab"\nCalculus BC - "calcbc"\nGrammar - "grammar"\nCollege Biology - "collegebio"\nCollege Chemistry - "collegechem"\nCollege Enviormental Science - "collegees"\nCollege Physics - "collegephysics"\nSAT Practice: - "sat"')
    options_help.place(x=600, y=270)

    back_button = tk.Button(text='Home', width=10, height=3, bg='#c197ff', fg='black', command=go_home)
    back_button.place(x=25, y=720)

    #keeps the window open and closes the loop
    window.mainloop()
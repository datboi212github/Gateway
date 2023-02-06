#importing tkinter libraries
import tkinter as tk
from tkinter import *
import webbrowser 

#imports the social library
import open_social
    
#Allows other scripts to run this script
def run_social():

    #sets window size and starts it maximized
    window = tk.Tk()
    window.geometry('1920x1080')
    window.state('zoomed')
    window.configure(bg='#ff96c9')

    font1 = ("Default", 25)
    greeting = tk.Label(text="Welcome to the Social Section", font=font1)
    greeting.place(x=550, y=25)

    global other

    #Converts the checkbox status into usable variables.
    def get_vars():
        discord = discordVar.get()
        instagram = instagramVar.get()
        snapchat = snapchatVar.get()
        facebook = facebookVar.get()
        twitter = twitterVar.get()
        youtube = youtubeVar.get()
        other = other_entry.get()

        if (discord == 1):
            open_social.initialize_discord()
        if (instagram == 1):
            open_social.initialize_instagram()
        if (snapchat == 1):
            open_social.initialize_snapchat()
        if (facebook == 1):
            open_social.initialize_facebook()
        if (twitter == 1):
            open_social.initialize_twitter()
        if (youtube == 1):
            open_social.initialize_youtube()
        if (other != ''):
            webbrowser.open_new_tab('https://'+other)                                                                                                   
            
    
    #allows the home button to send you to home
    def go_home():
        window.destroy()
        import main
        main.main_run()

    #the variable that stores wether the checkbox is checked or not
    twitterVar = IntVar()
    facebookVar = IntVar()
    snapchatVar = IntVar()
    instagramVar = IntVar()
    discordVar = IntVar()
    youtubeVar = IntVar()
    

    #code for the checkboxes
    twitter_button = Checkbutton(window, text='Open Twitter?', variable=twitterVar, onvalue=1, offvalue=0)
    twitter_button.place(x=720, y=420)

    discord_button = Checkbutton(window, text='Open Discord?', variable=discordVar, onvalue=1, offvalue=0)
    discord_button.place(x=720, y=220)

    facebook_button = Checkbutton(window, text='Open Facebook?', variable=facebookVar, onvalue=1, offvalue=0)
    facebook_button.place(x=720, y=370)

    snapchat_button = Checkbutton(window, text='Open Snapchat?', variable=snapchatVar, onvalue= 1, offvalue= 0,)
    snapchat_button.place(x=720, y=320)

    instagram_button = Checkbutton(window, text='Open Instagram?', variable=instagramVar, onvalue= 1, offvalue= 0,)
    instagram_button.place(x=720, y=270)

    youtube_button = Checkbutton(window, text='Open Youtube?', variable=youtubeVar, onvalue=1, offvalue=0)
    youtube_button.place(x=720, y=470)
    
    get_social_button = tk.Button(text='Open Socials', width=30, height=5, bg='#96ffcc', fg='black', command=get_vars)
    get_social_button.place(x=660, y=685)

    #Allows the user to input other websites that are not on the page.
    other_text = tk.Label(text='Input Other Website')
    other_text.place(x=720, y=520)
    other_entry = tk.Entry(fg='black', bg = 'white', width=50)
    other_entry.place(x=625, y=540)

    #code for the back button
    back_button = tk.Button(text='Home', width=10, height=3, bg='#96ffcc', fg='black', command=go_home)
    back_button.place(x=25, y=720)


    window.mainloop()
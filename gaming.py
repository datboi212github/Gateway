#importing tkinter libraries
import tkinter as tk
from tkinter import *

#importing gaming library
import open_gaming




def run_gaming():
    #sets window size and starts it maximized
    window = tk.Tk()
    window.geometry('1920x1080')
    window.state('zoomed')
    window.configure(bg='#00ebb6')

    font1 = ("Default", 25)
    greeting = tk.Label(text="Welcome to the Gaming Section", font=font1)
    greeting.place(x=550, y=25)

    

    def get_vars():
        game = open_game.get()
        discord = discordVar.get()
        spotify = spotifyVar.get()
        clip = ccVar.get()
        overwolf = overwolfVar.get()
        youtube = youtubeVar.get()
        

        if (game == "minecraft"):
            open_gaming.initialize_minecraft_launcher()
        elif (game == "btd6"):
            open_gaming.initialize_bloons_td()
        elif (game == "btdb2"):
            open_gaming.initialize_btdb2()
        elif (game == "riot"):
            open_gaming.initialize_riot()
        elif (game == "egl"):
            open_gaming.initialize_epic_games()
        elif (game == "steam"):
            open_gaming.initialize_steam()
        elif (game == "overwatch"):
            open_gaming.initialize_overwatch()
        
        if (discord == 1):
            open_gaming.initialize_discord()
        if (spotify == 1):
            open_gaming.initialize_spotify()
        if (clip == 1):
            open_gaming.initialize_clipchamp()
        if (overwolf == 1):
            open_gaming.initialize_overwatch()
        if (youtube == 1):
            open_gaming.intialize_youtube()

    def go_home():
        window.destroy()
        import main
        main.main_run()
    
    # discord_text = tk.Label(text='Do you want to open discord? ("yes" or "no")')
    # discord_text.place(x=625,y=200)
    # open_discord = tk.Entry(fg='black', bg='white', width=50)
    # open_discord.place(x=625, y=220)

    # spotify_text = tk.Label(text='Do you want to open spotify? ("yes" or "no")')
    # spotify_text.place(x=625, y=250)
    # open_spotify = tk.Entry(fg='black', bg='white', width=50)
    # open_spotify.place(x=625,y=270)

    # cc_text = tk.Label(text='Do you want to open clipchamp? ("yes" or "no")')
    # cc_text.place(x=625, y=300)
    # open_cc = tk.Entry(fg='black', bg='white', width=50)
    # open_cc.place(x=625,y=320)

    # youtube_text = tk.Label(text='Do you want to open youtube? ("yes" or "no")')
    # youtube_text.place(x=625, y=350)
    # open_youtube = tk.Entry(fg='black', bg='white', width=50)
    # open_youtube.place(x=625,y=370)

    game_text = tk.Label(text='Which game do you want to play?')
    game_text.place(x=680, y=100)
    open_game = tk.Entry(fg='black', bg='white', width=50)
    open_game.place(x=625, y=120)

    # overwolf_text = tk.Label(text='Do you want to open overwolf? ("yes" or "no")')
    # overwolf_text.place(x=625, y=400)
    # open_overwolf = tk.Entry(fg='black', bg='white', width=50)
    # open_overwolf.place(x=625, y=420)

    discordVar = IntVar()
    spotifyVar = IntVar()
    ccVar = IntVar()
    overwolfVar = IntVar()
    youtubeVar = IntVar()

    discord_button = Checkbutton(window, text='Open Discord?', variable=discordVar, onvalue=1, offvalue=0)
    discord_button.place(x=720, y=220)

    spotify_button = Checkbutton(window, text='Open Spotify?', variable=spotifyVar, onvalue=1, offvalue=0)
    spotify_button.place(x=720, y=270)

    cc_button = Checkbutton(window, text='Open Clipchamp?', variable=ccVar, onvalue= 1, offvalue= 0,)
    cc_button.place(x=720, y=320)

    overwolf_button = Checkbutton(window, text='Open Overwolf?', variable=overwolfVar, onvalue= 1, offvalue= 0,)
    overwolf_button.place(x=720, y=420)

    youtube_button = Checkbutton(window, text='Open Youtube?', variable=youtubeVar, onvalue=1, offvalue=0)
    youtube_button.place(x=720, y=370)

    get_games_button = tk.Button(text='Open Software', width=30, height=5, bg='#eb0035', fg='black', command=get_vars)
    get_games_button.place(x=660, y=685)

    game_list = tk.Label(text='Games Available (please note that you have to own these games):\nBloons TD 6: "btd6"\nMinecraft: "minecraft"\nBloons TD Battles 2: "btdb2"\nRiot Client: "riot"\nEpic Games Launcher: "egl"\nSteam: "steam"\nOverwatch: "overwatch"')
    game_list.place(x=600, y=500)

    back_button = tk.Button(text='Home', width=10, height=3, bg='#eb0035', fg='black', command=go_home)
    back_button.place(x=25, y=720)
    

    window.mainloop()
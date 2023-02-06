import webbrowser
from AppOpener import open

game_choice = ""

def example_syntax():
    print('here are some examples of games you can open: ')
    print('Bloons Tower Defense 6: "bloons td"')
    print('Minecraft: "minecraft launcher')
    print('Bloons Tower Defense Battles 2: "bloons td battles"')
    print('Riot Client: "riot client"')
    print('Epic Games Launcher: "epic games launcher"')
    print('Overwolf: "overwolf"')
    print('Battlefield 1: "battlefield t"')
    print('Overwatch: "overwatch"')
    #add more later

def initialize_game_opener():
    global game_choice
    game_choice = input('what game do you want to play?: ')
    
def initialize_bloons_td():
    open('bloons td')

def initialize_minecraft_launcher():
    open('minecraft launcher')

def initialize_btdb2():
    open('bloons td battles')

def initialize_riot():
    open('riot client')

def initialize_epic_games():
    open('epic games launcher')

def initialize_overwolf():
    open('overwolf')

def initialize_steam():
    open('steam')

def initialize_overwatch():
    open('overwatch')

def initialize_discord():
    open('discord') 

def initialize_spotify():
    open('spotify')

def initialize_clipchamp():
    open('clipchamp - video editor')

def intialize_youtube():
    webbrowser.open('https://youtube.com', new=2)


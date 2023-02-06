import webbrowser
from AppOpener import open

def example_syntax():
    print('These are the options for history \n')
    print('Ancient World History: "ancient history" \n')
    print('Modern World History: "modern history" \n')
    print('US History: "us history" \n')
    print('US Government and Civics: "us gov" \n')

def ancient_history():
    webbrowser.open('https://www.khanacademy.org/humanities/whp-origins', new=2)
def modern_history():
    webbrowser.open('https://www.khanacademy.org/humanities/whp-1750', new=2)
def us_history():
    webbrowser.open('https://www.khanacademy.org/humanities/us-history', new=2)
def us_gov():
    webbrowser.open('https://www.khanacademy.org/humanities/us-government-and-civics', new=2)
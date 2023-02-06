import webbrowser
from AppOpener import open

def example_syntax():
    print('here are the things you can do for coding: ')
    print('Learn Java: "learn java"')
    print('Learn Python: "learn python"')
    print('Learn C#: "learn csharp')
    print('Learn HTML: "learn html"')
    print('Write Java: "write java"')
    print('Write Python: "write python"')
    print('Write C#: "write csharp"')
    print('Write HTML: "write html"')
    print('Write Another Coding Language: "write other"')

def learn_java():
    webbrowser.open('https://docs.oracle.com/en/java/', new=2)
    webbrowser.open('https://www.codecademy.com/catalog/language/java', new=2)

def learn_python():
    webbrowser.open('https://docs.python.org/3/', new=2)
    webbrowser.open('https://www.codecademy.com/catalog/language/python', new=2)

def learn_csharp():
    webbrowser.open('https://learn.microsoft.com/en-us/dotnet/csharp/', new=2)
    webbrowser.open('https://www.codecademy.com/catalog/language/c-sharp', new=2)

def learn_html():
    webbrowser.open('https://developer.mozilla.org/en-US/docs/Web/HTML', new=2)
    webbrowser.open('https://www.codecademy.com/catalog/language/html-css', new=2)

def write_java():
    open('eclipse ide for java developers - -')

def write_python():
    open('idle python')

def write_csharp():
    open('unity hub') 

def write_html():
    open('notepad')

def write_other():
    open('visual studio code')

def open_stack_overflow():
    webbrowser.open('https://stackoverflow.com/', new=2)
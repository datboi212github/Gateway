import webbrowser
from AppOpener import open

def example_syntax():
    print('these are some of the science options \n')
    print('Middle School: Biology - "msbiology",  "earth and space", "physics" \n')
    print('High School: Biology - "hsbiology", Physics - "hsphysics" \n')
    print('College: Biology - "collegebio" \n Chemestry - "collegechem" \n Enviormental Science - "collegees" \n Physics - "collegephysics"')

def middle_bio():
    webbrowser.open('https://www.khanacademy.org/science/ms-biology', new=2)
def middle_earth_and_space():
    webbrowser.open('https://www.khanacademy.org/science/middle-school-earth-and-space-science', new=2)
def middle_physics():
    webbrowser.open('https://www.khanacademy.org/science/ms-physics', new=2)
def high_bio():
    webbrowser.open('https://www.khanacademy.org/science/high-school-biology', new=2)
def high_physics():
    webbrowser.open('https://www.khanacademy.org/science/high-school-physics', new=2)
def college_bio():
    webbrowser.open('https://www.khanacademy.org/science/ap-biology', new=2)
def college_chem():
    webbrowser.open('https://www.khanacademy.org/science/ap-chemistry-beta', new=2)
def college_ES():
    webbrowser.open('https://www.khanacademy.org/science/ap-college-environmental-science', new=2)
def college_physics():
    webbrowser.open('https://www.khanacademy.org/science/ap-college-physics-1', new=2)
from random import randint, shuffle
from guizero import Waffle, App, PushButton, Window, Text, Slider

"""This is supposed to be a simple minigame where you try to protect against fires"""


def startgame():
    startmenu.hide()
    app.show()

# Level size




# change "n", the ignition number


def ignitions(slider_value):
    n = int(slider_value)
    return n


# picks a box's adjacent box (includes diagonals): the x and y differences are less than 2, at least one of them is 1
def adjacent(pixel):  # and if it is neutral
    first_x = pixel.x
    first_y = pixel.y

    for second_pixel in pixels:
        second_x = second_pixel.x
        second_y = second_pixel.y
        x_dif = abs(first_x - second_x)
        y_dif = abs(first_y - second_y)
        if x_dif < 2 and y_dif < 2 and (x_dif == 1 or y_dif == 1) and second_pixel.color == "green":

            return second_pixel
    return pixel  # else it returns the original pixel


# dictates the fire spread: picks a random cell adjacent to a fire cell and makes it a fire cell, for all fire cells
def propagate():

    spreadables = []
    for source in pixels:

        if source.color == "#ff0000":
            spreadables.append(adjacent(source))

    for pixel in spreadables:

        pixel.color = '#ff0000'


"""This ignites the fire"""


def lighter():

    a = 2
    for i in range(0, a):
        x1 = randint(0, int(waffle.height)-1)
        y1 = randint(0, int(waffle.height)-1)
        waffle.set_pixel(x1, y1, "#ff0000")


def menubuttonthing():
    waffle.set_all("green")
    app.hide()
    scoremenu.hide()
    startmenu.show()


"""this resets the whole dam thing"""


def resetthething():
    waffle.set_all("green")
    lighter()
    app.show()
    scoremenu.hide()
    """i hid the score menu so that i could use the function
     for both buttons(the score menu and the game itself)"""


"""this kinda protects against the fire"""


def protec(a, b):
    thepixelcolor = waffle.get_pixel(a, b)
    if thepixelcolor != "#ff0000":
        waffle.set_pixel(a, b, "blue")


"""Score system"""


def scoresystem():
    score = 0
    for height in range(waffle.height):
        for lenght in range(waffle.width):
            if waffle.get_pixel(height, lenght) == "blue":
                score -= 1
            if waffle.get_pixel(height, lenght) == "green":
                score += 1
    app.hide()
    scoremenu.show()
    Actualscore.value = score


"""basic GUI setup"""
app = App(layout="grid", height=625, width=500)
# place waffle her if level size doesnt work

restbutton = PushButton(app, text="Reset/Start", command=resetthething, grid=[1, 2])
propagatebutton = PushButton(app, text="Propagate", command=propagate, grid=[1, 3])
scorebutton = PushButton(app, text="Score", command=scoresystem, grid=[1, 4])
"""Start menu stuff"""
startmenu = Window(app, title="Welcome", height=500, width=550)
introtext = Text(startmenu, text="Welcome to this tiny random game")
Instructions = Text(startmenu, size=9, text="Instructions: The objective is to protect as much of the forest(green) ")
Instructions2 = Text(startmenu, size=9,
                     text=" while using the least water (left mouse click that turns healthy forest into protected blue areas)")
Instructions3 = Text(startmenu, size=9, text="from the fire(red)")
# Fire speed
# Waffle size
# Start
startbutton = PushButton(startmenu, text="Start", command=startgame)
# credits
credits = Text(startmenu, text="Made by The Cool Guy 468 and Kidplayer_666", size=8)
"""Score stuff"""

scoremenu = Window(app)
Scoretext = Text(scoremenu, text="your score is")
Actualscore = Text(scoremenu, text="0")
restbutton2 = PushButton(scoremenu, text="Reset", command=resetthething)
menubutton = PushButton(scoremenu, text="Menu", command=menubuttonthing)
# Waffle setup here for experimental purposes, aka, level size testing
waffle = Waffle(app, pad=0, grid=[1, 1], height=20, width=20,
                color="green", command=protec, dim=25)
"""Pixel shuffler"""
pixels = []
for x in range(waffle.width):
    for y in range(waffle.height):
        pixels.append(waffle.pixel(x, y))
shuffle(pixels)
"""just starting the app"""
app.repeat(750, propagate)
startmenu.show()
scoremenu.hide()
app.hide()
app.display()

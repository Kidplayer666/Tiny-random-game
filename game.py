from random import randint, shuffle
from guizero import Waffle, App, PushButton, Window, Text

"""This is supposed to be a simple minigame where you try to protect against fires"""
def startgame():
    startmenu.hide()
    app.show()

# picks a box's adjacent box (includes diagonals): the x and y differences are less than 2, at least one of them is 1
def adjacent(pixel):                                                                           # and if it is neutral
    first_x = pixel.x
    first_y = pixel.y
    for second_pixel in pixels:
        second_x = second_pixel.x
        second_y = second_pixel.y
        x_dif = abs(first_x - second_x)
        y_dif = abs(first_y - second_y)
        if x_dif < 2 and y_dif < 2 and (x_dif == 1 or y_dif == 1) and second_pixel.color == "green":
            return second_pixel
    return pixel      # else it returns the original pixel

# dictates the fire spread: picks a random cell adjacent to a fire cell and makes it a fire cell, for all fire cells
def propagate():
    spreadables = []
    for source in pixels:
        if source.color == "red":
            spreadables.append(adjacent(source))
    for pixel in spreadables:
        pixel.color = "red"


"""This ignites the fire"""


def lighter():
    x1 = randint(0, 10)
    y1 = randint(0, 10)
    waffle.set_pixel(x1, y1, "red")
    x2 = randint(0, 10)
    y2 = randint(0, 10)
    waffle.set_pixel(x2, y2, "red")


"""this resets the whole dam thing"""


def resetthething():
    waffle.set_all("green")
    lighter()


"""this kinda protects against the fire"""


def protec(a, b):
    thepixelcolor = waffle.get_pixel(a, b)
    if thepixelcolor != "red":
        waffle.set_pixel(a, b, "blue")


"""basic GUI setup"""
app = App(layout="grid", height=625, width=500)
waffle = Waffle(app, pad=0, grid=[1, 1], height=20, width=20, color="green", command=protec, dim=25)
restbutton = PushButton(app, text="reset", command=resetthething, grid=[1, 2])
propagatebutton = PushButton(app, text="propagate", command=propagate, grid=[1, 3])
"""Start menu stuff"""
startmenu=Window(app, title="Welcome", height=200, width=550)
introtext=Text(startmenu, text="Welcome to this tiny random game")
Instructions=Text(startmenu, size=9, text="Instructions: The objective is to protect as much of the forest(green) ")
Instructions2=Text(startmenu, size=9, text=" while using the least water (left mouse click that turns healthy forest into protected blue areas)")
Instructions3=Text(startmenu, size=9, text="from the fire(red)")
startbutton=PushButton(startmenu, text="Start", command=startgame)
credits=Text(startmenu, text="Made by The Cool Guy 468 and Kidplayer_666", size=8)

pixels = []
for x in range(waffle.width):
    for y in range(waffle.height):
        pixels.append(waffle.pixel(x, y))
shuffle(pixels)

"""just starting the app"""
lighter()

app.repeat(750, propagate)
startmenu.show()
app.hide()
app.display()


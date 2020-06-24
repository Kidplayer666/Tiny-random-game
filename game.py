from random import randint, shuffle
from guizero import Waffle, App, PushButton, Text

"""This is supposed to be a simple minigame where you try to protect against fires"""


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
    scorer()          # updates the scoreboard


"""This ignites the fire"""


def lighter():
    x1 = randint(0, waffle.width - 1)
    y1 = randint(0, waffle.height - 1)
    waffle.set_pixel(x1, y1, "red")
    x2 = randint(0, waffle.width - 1)
    y2 = randint(0, waffle.height - 1)
    waffle.set_pixel(x2, y2, "red")
    scorer()    # updates the scoreboard


"""this resets the whole dam thing"""


def resetthething():
    waffle.set_all("green")
    lighter()


"""this kinda protects against the fire"""


def protec(a, b):
    thepixelcolor = waffle.get_pixel(a, b)
    if thepixelcolor != "red":
        waffle.set_pixel(a, b, "blue")
    scorer()       # updates the scoreboard


"""basic GUI setup"""
app = App(layout="grid", height=700, width=1000)
waffle = Waffle(app, pad=0, grid=[1, 1], height=10, width=10, color="green", command=protec, dim=50)
reset_button = PushButton(app, text="reset", command=resetthething, grid=[1, 2])
propagate_button = PushButton(app, text="propagate", command=propagate, grid=[1, 3])

pixels = []
for x in range(waffle.width):
    for y in range(waffle.height):
        pixels.append(waffle.pixel(x, y))
shuffle(pixels)

scoreboard = Text(app, f"Score = {waffle.height * waffle.width}", 20, "black", grid=[waffle.height, waffle.width])


def scorer():                     # score is the number of neutral cells
    score = waffle.width * waffle.height
    for pixel in pixels:
        if pixel.color == "blue":
            score -= 1
        if pixel.color == "red":
            score -= 1
    scoreboard.value = f"Score = {score}"


"""just starting the app"""
lighter()

app.repeat(1000, propagate)


"""above theres quite a high time before propagating due to error in function. Now it doesnt exist, theres a button 
to do it manually, this comment is to signal where to put this """
app.display()

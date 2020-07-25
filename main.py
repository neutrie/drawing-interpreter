from tkinter import *
from tkinter import filedialog

import figures

# tkinter setup
root = Tk()
root.title("Drawing")
root.geometry("800x600")
root.resizable(False, False)

# Default values
canvasColor = "white"
color = "black"
brushWidth = 1

# Canvas setup
canvas = Canvas(root, width=800, height=600, background=canvasColor)
canvas.pack()

# Instantiating drawing logic
# Draw(CANVAS, color, brushWidth, x1, y1, x2, y2)
line = figures.Line()

# Draw(CANVAS, color, brushWidth, x1, y1, x2, y2, x3, y3)
triangle = figures.Triangle()

# Draw(CANVAS, color, brushWidth, cx, cy, length)
equilateralTriangle = figures.EquilateralTriangle()


# Draw(CANVAS, color, brushWidth, cx, cy, width, height)
rectangle = figures.Rectangle()

# Draw(CANVAS, color, brushWidth, cx, cy, length)
square = figures.Square()


# Draw(CANVAS, color, brushWidth, cx, cy, verticalRadius, horizontalRadius)
ellipse = figures.Ellipse()

# Draw(CANVAS, color, brushWidth, cx, cy, radius)
circle = figures.Circle()


# Interpreter's additional functions
def ChangeCanvasColor(newColor):
    global canvasColor
    global canvas

    canvasColor = newColor
    canvas["background"] = canvasColor


def ChangeColor(newColor):
    global color

    color = newColor


def ChangeWidth(newWidth):
    global brushWidth
    brushWidth = float(newWidth)


def ResetCanvasColor():
    ChangeCanvasColor("white")


def ResetColor():
    ChangeColor("black")


def ResetWidth():
    ChangeWidth(1)


def ResetAll():
    global canvas

    ResetCanvasColor()
    ResetColor()
    ResetWidth()

    canvas.forget()
    canvas = Canvas(root, width=800, height=600, background=canvasColor)
    canvas.pack()


# returns path to a file
root.filename = filedialog.askopenfilename(initialdir=".", title="Select text file")

instructions = open(root.filename, "r").read().split('\n')
instructionsCount = len(instructions)

# Interpret

for instructionNumber in range(instructionsCount):
    currentInstruction = instructions[instructionNumber]
    words = currentInstruction.split(', ')

    if words[0].upper() == 'DRAW':
        if words[1].upper() == 'LINE':
            line.Draw(canvas, color, brushWidth, *words[2:])
        elif words[1].upper() == 'TRIANGLE':
            triangle.Draw(canvas, color, brushWidth, *words[2:])
        elif words[1].upper() == 'EQUILATERAL TRIANGLE':
            equilateralTriangle.Draw(canvas, color, brushWidth, *words[2:])
        elif words[1].upper() == 'RECTANGLE':
            rectangle.Draw(canvas, color, brushWidth, *words[2:])
        elif words[1].upper() == 'SQUARE':
            square.Draw(canvas, color, brushWidth, *words[2:])
        elif words[1].upper() == 'ELLIPSE':
            ellipse.Draw(canvas, color, brushWidth, *words[2:])
        elif words[1].upper() == 'CIRCLE':
            circle.Draw(canvas, color, brushWidth, *words[2:])

    elif words[0].upper() == 'CHANGE':
        if words[1].upper() == 'CANVAS COLOR':
            ChangeCanvasColor(words[2])
        elif words[1].upper() == 'COLOR':
            ChangeColor(words[2])
        elif words[1].upper() == 'WIDTH':
            ChangeWidth(words[2])

    elif words[0].upper() == 'RESET':
        if words[1].upper() == 'CANVAS COLOR':
            ResetCanvasColor()
        elif words[1].upper() == 'COLOR':
            ResetColor()
        elif words[1].upper() == 'WIDTH':
            ResetWidth()
        elif words[1].upper() == 'ALL':
            ResetAll()

root.mainloop()
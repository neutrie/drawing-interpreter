import math

class Line:
    def Draw(self, canvas, color, brushWidth, *args):
        x1, y1, x2, y2 = map(float, args)

        canvas.create_line(x1, y1, x2, y2, fill=f'{color}', width=brushWidth)

# Triangles
class Triangle(Line):
    def Draw(self, canvas, color, brushWidth, *args):
        x1, y1, x2, y2, x3, y3 = map(float, args)

        super(Triangle, self).Draw(canvas, color, brushWidth, x1, y1, x2, y2)
        super(Triangle, self).Draw(canvas, color, brushWidth, x2, y2, x3, y3)
        super(Triangle, self).Draw(canvas, color, brushWidth, x3, y3, x1, y1)

class EquilateralTriangle(Triangle):
    def Draw(self, canvas, color, brushWidth, *args):
        cx, cy, length = map(float, args)

        height = length * math.sqrt(3) / 2
        x1 = cx
        y1 = cy - (2/3 * height)
        x2 = cx - length / 2
        y2 = cy + (1/3 * height)
        x3 = cx + length / 2
        y3 = y2
        
        super(EquilateralTriangle, self).Draw(canvas, color, brushWidth, x1, y1, x2, y2, x3, y3)

# Rectangles
class Rectangle(Line):
    def Draw(self, canvas, color, brushWidth, *args):
        cx, cy, width, height = map(float, args)

        x1 = cx - width / 2
        y1 = cy - height / 2
        x2 = cx + width / 2
        y2 = y1
        x3 = x2
        y3 = cy + height / 2
        x4 = x1
        y4 = y3

        super(Rectangle, self).Draw(canvas, color, brushWidth, x1, y1, x2, y2)
        super(Rectangle, self).Draw(canvas, color, brushWidth, x2, y2, x3, y3)
        super(Rectangle, self).Draw(canvas, color, brushWidth, x3, y3, x4, y4)
        super(Rectangle, self).Draw(canvas, color, brushWidth, x4, y4, x1, y1)

class Square(Rectangle):
    def Draw(self, canvas, color, brushWidth, *args):
        cx, cy, length = map(float, args)

        super(Square, self).Draw(canvas, color, brushWidth, cx, cy, length, length)


# Ellipses
class Ellipse:
    def Draw(self, canvas, color, brushWidth, *args):
        cx, cy, vertR, horR = map(float, args)

        x1 = cx - horR
        y1 = cy - vertR
        x2 = cx + horR
        y2 = cy + vertR

        canvas.create_oval(x1, y1, x2, y2, outline=f'{color}', width=brushWidth)


class Circle(Ellipse):
    def Draw(self, canvas, color, brushWidth, *args):
        cx, cy, R = map(float, args)
        
        super(Circle, self).Draw(canvas, color, brushWidth, cx, cy, R, R)
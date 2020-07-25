# Drawing interpreter
![alt text](demo_pic.png "Christmas tree (i tried my best...)")
##### Drawing interpreter is a step by step interpreter of basic drawing commands.
Made in purpose of mastering basic aspects of inheritance in OOP.

### **How to use**:
* Launch main file
* Select text file which contains instructions for interpreter
* Done

### **Supported instructions:**

##### Drawing:
* **draw, line, *x1*, *y1*, *x2*, *y2***
> Draws a line from (x1, y1) to (x2, y2) on the canvas with selected color and brush width.
* **draw, triangle, *x1*, *y1*, *x2*, *y2*, *x3*, *y3***
> Draws a triangle with the vertices in (x1, y1), (x2, y2), (x3, y3) on the canvas with selected color and brush width.
* **draw, equilateral triangle, *cx*, *cy*, *length***
> Draws an equilateral triangle with the center at (cx, cy) on the canvas with selected color, side length and brush width.
* **draw, rectangle, *cx*, *cy*, *width*, *height***
> Draws a rectangle with the center at (cx, cy) on the canvas with selected color, width, height and brush width.
* **draw, square, *cx*, *cy*, *length***
> Draws a square with the center at (cx, cy) on the canvas with selected color, side length and brush width.
* **draw, ellipse, *cx*, *cy*, *verticalRadius*, *horizontalRadius***
> Draws an ellipse with the center at (cx, cy) on the canvas with selected color, veritcal radius, horizontal radius and brush width.
* **draw, circle, *cx*, *cy*, *radius***
> Draws a circle with the center at (cx, cy) on the canvas with selected color, radius and brush width.

##### Changing:
* **change, canvas color, *newColor***
> Immediately changes current canvas color to the new one.
* **change, color, *newColor***
> Changes current brush color to the new one.
* **change, width, *newWidth***
> Changes current brush width to the new one.

##### Resetting:
* **reset, canvas color**
> Immediately changes current canvas color white.
* **reset, color**
> Changes current brush color to black.
* **reset, width**
> Changes current brush width to 1.
* **reset, all**
> Clears the canvas and resets canvas color, brush color and brush width.
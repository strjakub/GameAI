from Vector import Vector
from Square import Square
from Map import Map, graininess
from math import floor
import tkinter
import keyboard

zoom = 3
width = 200

if __name__ == '__main__':
    y = Map()
    x = Square(Vector(5, 7 * graininess - 1), y)
    top = tkinter.Tk()
    grid = y.to_grid()
    canvas = tkinter.Canvas(top, bg="lightblue", height=len(grid) * zoom, width=width * zoom)
    canvas.pack()
    dash = 0
    while True:
        if keyboard.is_pressed('space'):
            x.jump()

        x.move2()
        if x.position.x + graininess + 5 >= len(grid[0]):
            exit(0)
        if not x.position.x + width >= len(grid[0]):
            dash += floor(1 * graininess / 5)

        canvas.delete("all")
        for j in range(len(grid)):
            for i in range(width):
                if x.contain_square_body(i + dash, j):
                    canvas.create_rectangle(i * zoom, j * zoom, (i + 1) * zoom, (j + 1) * zoom, fill="green",
                                            outline="green")
                elif grid[j][dash + i] == 2:
                    canvas.create_rectangle(i * zoom, j * zoom, (i + 1) * zoom, (j + 1) * zoom, fill="red",
                                            outline="red")
                elif grid[j][dash + i] == 1:
                    canvas.create_rectangle(i * zoom, j * zoom, (i + 1) * zoom, (j + 1) * zoom, fill="black",
                                            outline="black")
        canvas.update()

        if x.is_dead() > 0:
            break

    top.mainloop()

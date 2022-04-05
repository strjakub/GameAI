from Vector import Vector
from Square import Square
from Map import Map
import tkinter
import keyboard
import random

if __name__ == '__main__':
    y = Map()
    x = Square(Vector(5, 49), y)
    top = tkinter.Tk()
    grid = y.to_grid()
    canvas = tkinter.Canvas(top, bg="lightblue", height=len(grid) * 10, width=600)
    canvas.pack()
    dash = 0
    while True:
        if keyboard.is_pressed('space'):
            x.jump()

        x.move()
        if x.position.x + 60 >= len(grid[0]):
            break

        canvas.delete("all")
        for j in range(len(grid)):
            for i in range(60):
                if x.contain_square_body(i + dash, j):
                    flag = random.randint(0, 2)
                    if flag == 0:
                        canvas.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill="green", outline="green")
                    if flag == 1:
                        canvas.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill="lightgreen", outline="lightgreen")
                    if flag == 2:
                        canvas.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill="darkgreen", outline="darkgreen")
                elif grid[j][dash + i] == 2:
                    canvas.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill="red", outline="red")
                elif grid[j][dash + i] == 1:
                    canvas.create_rectangle(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10, fill="black", outline="black")
        canvas.update()

        if x.is_dead() > 0:
            break
        dash += 3

    top.mainloop()

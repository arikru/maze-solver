from graphics import *

def main():
    win = Window(800, 600)
    cell = Cell(Point(30,40), Point(50,80), win)
    cell.draw("black")
    win.wait_for_close()


main()

from graphics import *

def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(10, 10, 20, 50)
    win.wait_for_close()


main()

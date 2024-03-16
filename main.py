from graphics import *

def main():
    win = Window(800, 600)
    cell = Cell(30, 50, 50, 70, win, has_top_wall=False, has_bottom_wall=False)
    cell.draw("black")
    cell = Cell(80,100, 110, 130, win, has_left_wall=False, has_right_wall=False)
    cell.draw("black")
    win.wait_for_close()


main()

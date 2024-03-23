from graphics import *

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.draw(100, 100, 200, 200)
    cell2 = Cell(win)
    cell2.draw(0, 100, 100, 200)
    cell1.draw_move(cell2, undo=True)
    win.wait_for_close()


main()

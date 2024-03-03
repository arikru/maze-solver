from graphics import *

def main():
    win = Window(800, 600)
    line_1 = Line(Point(10,10), Point(50,10))
    line_2 = Line(Point(50,10), Point(500,10))
    win.draw_line(line_1, "red")   
    win.draw_line(line_2, "black")   
    win.wait_for_close()


main()

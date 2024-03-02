from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        pass

from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, {"width": width, "height": height})
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        # x=0 is the left of the screen, y=0 is the top
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(
                self.start.x, 
                self.start.y, 
                self.end.x, 
                self.end.y, 
                fill=fill_color, 
                width=2
        )
        canvas.pack(fill=BOTH, expand=True)


class Cell:
    def __init__(self,x1, y1, x2, y2, win,
                 has_left_wall=True, 
                 has_right_wall=True,
                 has_top_wall=True,
                 has_bottom_wall=True,
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1 
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

         
    def draw(self, fill_color):
        y_offset = self._y2 - self._y1
        x_offset = self._x2 - self._x1 

        if self.has_left_wall:
            self._win.canvas.create_line(
                self._x1, 
                self._y1, 
                self._x2 - x_offset, 
                self._y2, 
                fill=fill_color,
                width=2
            )


        if self.has_right_wall:
            self._win.canvas.create_line(
                self._x1 + x_offset, 
                self._y1, 
                self._x2, 
                self._y2, 
                fill=fill_color,
                width=2
            )


        if self.has_top_wall:
            self._win.canvas.create_line(
                self._x1, 
                self._y1, 
                self._x2, 
                self._y2 - y_offset, 
                fill=fill_color,
                width=2
            )


        if self.has_bottom_wall:
            self._win.canvas.create_line(
                self._x1, 
                self._y1 + x_offset, 
                self._x2, 
                self._y2, 
                fill=fill_color,
                width=2
            )

        self._win.canvas.pack(fill=BOTH, expand=True)

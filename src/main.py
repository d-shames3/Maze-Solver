from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    
    point_1 = Point(50, 50)
    point_2 = Point(100, 100)
    point_3 = Point(200, 30)
    point_4 = Point(25, 300)

    line_1 = Line(point_1, point_2)
    line_2 = Line(point_3, point_4)

    win.draw_line(line_1, "red")
    win.draw_line(line_2, "blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()
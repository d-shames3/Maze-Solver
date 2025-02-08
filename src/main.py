from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell_1 = Cell(30, 70, 30, 50, win, has_top_wall=False, has_right_wall=False)
    cell_2 = Cell(70, 110, 30, 50, win, has_right_wall=False, has_left_wall=False)
    cell_3 = Cell(110, 150, 30, 50, win, has_left_wall=False, has_bottom_wall=False)
    cell_4 = Cell(110, 150, 50, 70, win, has_top_wall=False)

    cell_1.draw("white")
    cell_2.draw("white")
    cell_3.draw("white")
    cell_4.draw("white")

    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_3)
    cell_3.draw_move(cell_4)

    win.wait_for_close()

if __name__ == "__main__":
    main()
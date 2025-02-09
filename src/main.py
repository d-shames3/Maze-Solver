from window import Window
from maze import Maze

def main():
    num_rows = 5
    num_cols = 5
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    seed = 3
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, seed, win)
    #maze._cells[0][0].draw_move(maze._cells[1][0])
    maze.solve_maze()

    win.wait_for_close()

if __name__ == "__main__":
    main()
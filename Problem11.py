import sys
import numpy as np

def process_input(args):
    with open(args[0]) as f:
        lines = f.readlines()
        grid = np.empty((20, 20), dtype = int)
        for i in range(len(lines)):
            grid[i] = lines[i].split(' ')
        return grid

def main():
    args = sys.argv[1:]
    grid = process_input(args)
    max = 0
    print(grid[6,8]*grid[7,9] * grid[8][10] * grid[9][11])
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i < len(grid) - 3):
                prod = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
                if prod > max:
                    max = prod
                    print(i, j, max)

            if (j < len(grid[0]) - 3):
                prod = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
                if prod > max:
                    max = prod
                    print(i, j, max)

            if (j < len(grid[0]) - 3) and (i < len(grid) - 3):
                prod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
                if prod > max:
                    max = prod
                    print(i, j, max)
            if (j > 3) and (i < len(grid) - 3):
                prod = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
                if prod > max:
                    max = prod
                    print(i, j, max)
    print(max)

if __name__ == "__main__":
    main()

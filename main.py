#!/usr/bin/env python3

import random
import sys
import time
import os
import json
import numpy as np

class configurations:
	# Importing all the configurations
    with open('config.json') as config_file:
        data = json.load(config_file)

    patterns = data['patterns']
	# Still Lifes
    Block = np.array(patterns['block'])
    Beehive = np.array(patterns['bee-hive'])
    Loaf = np.array(patterns['loaf'])
    Boat = np.array(patterns['boat'])
    Tub = np.array(patterns['tub'])

	# Oscillators
    Blinker = np.array(patterns['blinker'])
    Toad = np.array(patterns['toad'])
    Beacon = np.array(patterns['beacon'])

	# Spaceships
    Glider = np.array(patterns['glider'])
    LWSpaceship = np.array(patterns['lwss'])
    MWSpaceship = np.array(patterns['mwss'])
    HWSpaceship = np.array(patterns['hwss'])
    d = {1: Block, 2: Beehive, 3: Loaf, 4: Boat, 5: Tub, 6: Blinker, 7: Toad, 8: Beacon, 9: Glider, 10: LWSpaceship, 11: MWSpaceship, 12: HWSpaceship}







class GOL:

    def __init__(self,test =False):
        # Get the number of rows and columns for the GOL grid
        self.rows = self.get_integer_value("Enter the number of rows (10-60): ", 10, 60)
        self.cols = self.get_integer_value("Enter the number of cols (10-118): ", 10, 118)
        self.confi = configurations()
        # Get the number of generations that GOL should run for
        if test == False:
            self.generations = self.get_integer_value("Enter the number of generations (1-100000): ", 1, 100000)
            

            self.resize_console(self.rows, self.cols)
            
            np.random.seed = self.confi.data['random_seed']

            
            print("Please enter the number (1-12) of the pattern you would like to add to the grid or enter 00 for random.")
            print("1 Block \n2 Beehive\n3 Loaf\n4 Boat\n5 Tub\n6 Blinker\n7 Toad\n8 Beacon\n9 Glider\n10 Lwss\n11 Mwss\n12 Hwss\n00 Random grid")
            self.selection = int(input("Here comes your Choice: "))


    def clear_console(self):

        if sys.platform.startswith('win'):
            os.system("cls")
        elif sys.platform.startswith('linux'):
            os.system("clear")
        else:
            print("Unable to clear terminal. Your OS isn't supported.\n\r")


    def resize_console(self,rows, cols):
        """
        Re-sizes the console to the size of rows x columns
        
        Params:
        rows (int) - number of rows for the console to re-size to
        cols (int) - number of columns for the console to re-size to
        """

        if cols < 32:
            cols = 32

        if sys.platform.startswith('win'):
            command = "mode con: cols={0} lines={1}".format(cols + cols, rows + 5)
            os.system(command)
        elif sys.platform.startswith('linux'):
            command = "\x1b[8;{rows};{cols}t".format(rows=rows + 3, cols=cols + cols)
            sys.stdout.write(command)
        else:
            print("Unable to resize terminal. Your OS isn't supported.\n\r")


    def create_initial_grid(self,ob, i,j, rand = True):
        """
        Makes a random list of lists containing 0s and 1s to represent the cells in CGOL.

        Params:
        rows (int) - The number of rows that the Game of Life grid will have
        cols (int) - The number of columns that the Game of Life grid will have
        
        returns-  list of lists containing 1s for live cells and 0s for dead cells
        """
        
        if rand == True:
            grid= []
            for row in range(self.rows):
                grid_rows = []
                for col in range(self.cols):
                    if random.randint(0, 7) == 0:
                        grid_rows += [1]
                    else:
                        grid_rows += [0]
                grid += [grid_rows]
            return grid
        else:
            grid = np.zeros((self.rows, self.cols))
            w, h = ob.shape
            i = np.clip(i, 0, self.rows - w - 1)
            j = np.clip(j, 0, self.cols - h - 1)
            # print("hey", grid)
            grid[i:i+w, j:j+h] = ob

            return grid


    def print_grid(self,rows, cols, grid, generation):
        """
        
        Params:
        grid (int[][]) -  list of lists that will be used to represent the GOL grid
        generation (int) - current generation of the GOL grid
        """

        self.clear_console()

        # single output string used to help in reducing the flickering due to printing multiple lines
        output_str = ""

        
        output_str += "Generation {0} - To exit the program early press <Ctrl-C>\n\r".format(generation)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    output_str += "  "
                else:
                    output_str += "👾 "
            output_str += "\n\r"
        print(output_str, end=" ")


    def create_next_grid(self,rows, cols, grid, next_grid, test = False):
        """
        Analyzes the current generation of the Game of Life grid and determines what cells live and die in the next
        generation of the Game of Life grid.

        Params:
        next_grid (int[][]) - list of lists that will be used to represent the next generation of the GOL grif
        """

        for row in range(rows):
            for col in range(cols):
                # number of live cells adjacent to the cell at grid[row][col]
                live_neighbors = self.get_live_neighbors(row, col, rows, cols, grid)

                # Underpopulation and overpopulation
                if live_neighbors < 2 or live_neighbors > 3:
                    next_grid[row][col] = 0
                # Reproduction
                elif live_neighbors == 3 and grid[row][col] == 0:
                    next_grid[row][col] = 1
                # If the number of surrounding live cells is 3 and the cell at grid[row][col] is alive keep it alive
                else:
                    next_grid[row][col] = grid[row][col]
        if test == True:
            return next_grid


    def get_live_neighbors(self,row, col, rows, cols, grid):
        """
        counts the number of live cells surrounding a center cell at grid[row][cell].

        return (int) - The number of live cells surrounding the cell at grid[row][cell]
        """

        life_sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # making sure to count the center cell located at grid[row][col]
                if not (i == 0 and j == 0):
                    life_sum += grid[((row + i) % rows)][((col + j) % cols)]
        return life_sum


    def grid_changing(self,rows, cols, grid, next_grid):
        """
        checks to see if the current generation GOL grid is the same as the next generation's grid.

        return (boolean) - whether the current generation grid is the same as the next generation grid
        """

        for row in range(rows):
            for col in range(cols):
                if not grid[row][col] == next_grid[row][col]:
                    return True
        return False


    def get_integer_value(self,prompt, low, high):
        """
        asks the user for integer input and between given bounds low and high.

        Params:
        prompt (string) - string to prompt the user for input with
        low (int) - low bound that the user must stay within
        high (int) - high bound that the user must stay within
        
        return: valid input value that the user entered
        """

        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print("Input was not a valid integer value.")
                continue
            if value < low or value > high:
                print("Input was not inside the bounds (value <= {0} or value >= {1}).".format(low, high))
            else:
                break
        return value


    def run_game(self):
        """
        asks the user for input to  number of generations.

        """

        self.clear_console()

        rand1 = False
        # Create the initial random GOL grids
        if self.selection==00:
            print("hey random")
            current_generation = self.create_initial_grid(None, 1,3, True)
        else:
            current_generation = self.create_initial_grid(self.confi.d[self.selection], 1,3, False)
        
        next_generation = self.create_initial_grid(None, 1,3, True)

        # Run Game of Life sequence
        gen = 1
        for gen in range(1, self.generations + 1):
            if not self.grid_changing(self.rows, self.cols, current_generation, next_generation):
                break
            self.print_grid(self.rows, self.cols, current_generation, gen)
            self.create_next_grid(self.rows, self.cols, current_generation, next_generation)
            time.sleep(1 / 5.0)
            current_generation, next_generation = next_generation, current_generation

        self.print_grid(self.rows, self.cols, current_generation, gen)
        input("Press <Enter> to exit.")



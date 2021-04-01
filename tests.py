from main import GOL
import json
import numpy as np
import unittest

class TestGolMethods(unittest.TestCase):

	def setUp(self):
		self.g = GOL(test = True)
		self.rows = self.g.rows
		self.cols = self.g.cols

	def test_created_grid(self):
		np.testing.assert_array_equal(self.g.create_initial_grid(np.array([[]]),1,3,False),np.zeros((self.rows,self.cols)))

	def test_pattern_placement(self):
		grid = self.g.create_initial_grid(self.g.confi.Beehive, 10,10, False)
		test_grid = np.zeros((self.rows,self.cols))
		test_grid[10:15, 10:16] = np.array([[0, 0, 0, 0, 0, 0],[0, 0, 1, 1, 0, 0],[0, 1, 0, 0, 1, 0],[0, 0, 1, 1, 0, 0],[0, 0, 0, 0, 0, 0]])
		np.testing.assert_array_equal(grid, test_grid)

	def test_still_life(self):
		grid = self.g.create_initial_grid(self.g.confi.Block, 0,0, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[1:3,1:3] = np.array([[1, 1], [1, 1]])
		np.testing.assert_array_equal(next_grid, test_grid)

		grid = self.g.create_initial_grid(self.g.confi.Beehive, 10,10, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[11, 12:14] = np.array([[1, 1]])
		test_grid[12, 11] = 1
		test_grid[12, 14] = 1
		test_grid[13, 12:14] = 1
		np.testing.assert_array_equal(next_grid, test_grid)

		grid = self.g.create_initial_grid(self.g.confi.Loaf, 10,10, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[11, 12:14] = np.array([[1, 1]])
		test_grid[12, 11] = 1
		test_grid[12, 14] = 1
		test_grid[13, 12] = 1
		test_grid[13, 14] = 1
		test_grid[14, 13] = 1
		np.testing.assert_array_equal(next_grid, test_grid)

		grid = self.g.create_initial_grid(self.g.confi.Boat, 10,10, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[11, 11:13] = np.array([[1, 1]])
		test_grid[12, 11] = 1
		test_grid[12, 13] = 1
		test_grid[13, 12] = 1
		np.testing.assert_array_equal(next_grid, test_grid)

		grid = self.g.create_initial_grid(self.g.confi.Tub, 10,10, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[11, 12] = np.array([[1]])
		test_grid[12, 11] = 1
		test_grid[12, 13] = 1
		test_grid[13, 12] = 1
		np.testing.assert_array_equal(next_grid, test_grid)
	

	def test_still_oscillators(self):
		grid = self.g.create_initial_grid(self.g.confi.Blinker, 0,0, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[0:3, 2] = np.array([1,1,1])
		np.testing.assert_array_equal(next_grid, test_grid)

		grid = self.g.create_initial_grid(self.g.confi.Toad, 1,3, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[1, 6] = 1
		test_grid[2,4] = 1
		test_grid[2,7] = 1
		test_grid[3,4] = 1
		test_grid[3,7] = 1
		test_grid[4,5] = 1
		np.testing.assert_array_equal(next_grid, test_grid)

		test_grid[2:4, 4] = np.array([1,1])
		test_grid[2:4, 7] = np.array([1,1])
		test_grid[4, 5] = 1
		np.testing.assert_array_equal(next_grid, test_grid)

		grid = self.g.create_initial_grid(self.g.confi.Beacon, 1,3, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[1, 3:5] = np.array([[1, 1]])
		test_grid[2, 3] = 1
		test_grid[3, 6] = 1
		test_grid[4, 5:7] = np.array([[1, 1]])
		np.testing.assert_array_equal(next_grid, test_grid)


	def test_still_spaceships(self):
		grid = self.g.create_initial_grid(self.g.confi.Glider, 0,0, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[0,1] = 1
		test_grid[1:3,2] = np.array([1,1])
		test_grid[2,0:2] = np.array([[1, 1]])
		np.testing.assert_array_equal(next_grid, test_grid)

		grid = self.g.create_initial_grid(self.g.confi.LWSpaceship, 1,3, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[4, 9:11] = np.array([[1, 1]])
		test_grid[5, 8:10] = np.array([[1, 1]])
		test_grid[5, 11:13] = np.array([[1, 1]])
		test_grid[6, 9:13] = np.array([[1, 1, 1, 1]])
		test_grid[7, 10:12] = np.array([[1, 1]])
		np.testing.assert_array_equal(next_grid, test_grid)
		
		grid = self.g.create_initial_grid(self.g.confi.MWSpaceship, 1,3, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[6, 9:11] = np.array([[1, 1]])
		test_grid[7, 8:10] = np.array([[1, 1]])
		test_grid[7, 11:14] = np.array([[1, 1, 1]])
		test_grid[8, 9:14] = np.array([[1, 1, 1, 1, 1]])
		test_grid[9, 10:13] = np.array([[1, 1, 1]])
		np.testing.assert_array_equal(next_grid, test_grid)
		

		grid = self.g.create_initial_grid(self.g.confi.HWSpaceship, 1,3, False)
		test_grid = np.zeros((self.rows,self.cols))
		next_grid = self.g.create_next_grid(self.rows, self.cols, grid,np.zeros((self.rows,self.cols)),True)
		test_grid[5, 11:13] = np.array([[1, 1]])
		test_grid[6, 10:12] = np.array([[1, 1]])
		test_grid[6, 13:17] = np.array([[1, 1, 1, 1]])
		test_grid[7, 11:17] = np.array([[1, 1, 1, 1, 1, 1]])
		test_grid[8, 12:16] = np.array([[1, 1, 1, 1]])
		np.testing.assert_array_equal(next_grid, test_grid)


if __name__ == "__main__":
	unittest.main()
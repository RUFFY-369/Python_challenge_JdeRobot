from main import GOL
import json
import numpy as np
import time

print("----------------------------------------------------------")
print("               BEGIN THE GAME OF LIFE                     ")
print("----------------------------------------------------------")
iterations = int(input("Please enter the number of iterations (int) you want to perform: "))
iterations = np.clip(iterations, 10, 1000)

for i in range(iterations):
	print("Iteration "+str(i+1))
	g = GOL()
	g.run_game()
	print("Press Ctrl+C at any point to exit. The program shall automatically exit after the maximum iterations.")

print("------------TIMES UP---------------")


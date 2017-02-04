# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Naked Twins is a technique which helps to reduce numbers from other units. Naked twins is at the same level as other techniniques like elimination and only_choice. 
Contraint Propogation is a methodology. In this methodology, for a given solution space, we create constraints so that we reduce the solution space. 
Since there are three techniques which we can use for Sudoku hence we have to apply them in sequence and in a loop till there is no other reduction in solution space.
After we have reached the maximumally constraint solution space and there is no scope of further constraints, we implement depth first search to solve the Sudoku problem


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: In Diagonal Sudoku problem, there is additional constraint on the diagonals. In regular sudoku problem, there are nine 3x3 squares and each box is a part of a square or a unit. Similarly every vertical column and horizontal row has 9 elements and represent units.
Each unit has a property that it can only have 1-9 digits only once. Each box will have 3 units(square, row and column). With diagonal sudoku, box on diagonals will have 4 units and the center box will have 5 units.
In the code, we create a list of units and we include diagonals in the list of units. 
We ensure that each unit follows the rule and techniques like elimination, only_choice and naked_twins and also take the diagonals as a unit to enfore the rule

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in function.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
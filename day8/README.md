To solve this problem, I created a function that calculates the scenic score for each tree in the given grid. Then, iterated through the grid and find the highest scenic score.
The highest_scenic_score function follows a similar structure, iterating through each tree in the grid and calling the scenic_score function to calculate the scenic score for each tree. It keeps track of the maximum scenic score found so far and returns it at the end.
The function called scenic_score that takes three arguments: grid, row, and col. grid is a 2D list representing the tree heights, row and col are the coordinates of the tree.
I get the height of the tree at the given row and col coordinates.
Then, defines a list of tuples representing the four directions I need to check: up, right, down, and left. Each tuple contains the row and column offsets for moving in that direction
Then, initiated the score variable to be one
Started a loop that iterates over the directions list. In each iteration, dr and dc represent the row and column offsets for the current direction.
create a conditional statement the continue looping until the conditions are not met
increasing the score to be +1 if the conditions are met.
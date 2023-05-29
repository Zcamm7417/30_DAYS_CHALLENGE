To solve this problem, I followed these steps:
Initialize the head and tail positions as (0, 0).
Create a set to store the visited positions by the tail.
Iterate through the series of motions and update the head position accordingly.
After each motion, check if the tail needs to be moved and update its position.
I updated the tail's position after processing all the steps in a single direction instead of updating it after each step
The tail should move diagonally only when it's not in the same row or column as the head
Add the tail's position to the visited set.
Return the length of the visited set.

I defines a function read_motions_from_file that takes a file path as input, reads the file line by line, and appends the direction and steps as a tuple to the motions list. Finally, it returns the list of motions. You can then use this list with the simulate_rope function to get the result
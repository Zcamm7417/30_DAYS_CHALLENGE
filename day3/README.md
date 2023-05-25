part 1
Studied the data, I open the txt file and read it into rucksacks and splited it with new line
Defined a function "calculate_priority"
giving the function conditional statement of a-z is 1-26 and A-Z is 27+
Then, I further defined another function "find_common_items"
setting variable total_priority to zero
I gave a condition setting first_conpartment to be the whole lenght of the present line to be divided by two, while the second compartment is the remaining on that line.
further check if any letter in first_compartment intersect with any letter in second compartment eqauting it to variable "common_items"
then, I iterated through the stored list of common_item and pass in the function calculate_priority on it.
which will keep summing the values together.
then finally, I returned the total_priority.

part 2
conditions have been updated to badge of three.
here, I look for letters that appears in all lines of badges of three, 0, 1, 2
then pass in the function "calculate_priority" and returned the variable "total_priority"

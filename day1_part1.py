# Read the contents of the text file
with open("day1_data.txt", "r") as file:
    input_data = file.read().strip()[3:-3]

elves_inventory = input_data.strip().split("\n\n")
max_calories = 0
elf_with_max_calories = 0
for index, inventory in enumerate(elves_inventory, start=1):
    calories = sum(int(calorie) for calorie in inventory.split("\n"))
    if calories > max_calories:
        max_calories = calories
        elf_with_max_calories = index

print(f"The Elf carrying the most calories is Elf {elf_with_max_calories}.")
print(f"Carrying a total of {max_calories} calories.")
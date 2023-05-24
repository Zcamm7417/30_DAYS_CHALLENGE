def calculate_priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27

def find_common_items(rucksacks):
    total_priority = 0

    for rucksack in rucksacks:
        first_compartment = set(rucksack[:len(rucksack)//2])
        second_compartment = set(rucksack[len(rucksack)//2:])
        common_items = first_compartment.intersection(second_compartment)

        for item in common_items:
            priority = calculate_priority(item)
            total_priority += priority

    return total_priority

with open("day3_data.txt", "r") as file:
    rucksacks = file.read().split("\n")
total_priority = find_common_items(rucksacks)
print(f"The sum of priorities for the common items is: {total_priority}")

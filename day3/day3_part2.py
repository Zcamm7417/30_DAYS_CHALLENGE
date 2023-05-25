def calculate_priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27


def find_badge_items(rucksacks):
    total_priority = 0

    pairs = [rucksacks[i:i+3] for i in range (0, len(rucksacks), 3)]
    for pair in pairs:
        common_items = set(pair[0]) & set(pair[1]) & set(pair[2])    

        for item in common_items:
            priority = calculate_priority(item)
            total_priority += priority

    return total_priority

with open("day3_data.txt", "r") as file:
    rucksacks = file.read().split("\n")
total_priority = find_badge_items(rucksacks)
print(f"The sum of priorities for the badge items is: {total_priority}")
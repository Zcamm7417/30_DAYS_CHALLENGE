import re

def parse_directory_listing(listing):
    filesystem = {}
    current_dir = filesystem
    stack = [current_dir]

    for line in listing:
        if line.startswith("dir "):
            directory_name = line[4:]
            current_dir[directory_name] = {}
            current_dir = current_dir[directory_name]
            stack.append(current_dir)
        elif re.match(r"\d+ \w+", line):
            file_size, file_name = line.split()
            current_dir[file_name] = int(file_size)
        # elif line.startswith("$ cd "):
        #     directory_name = line[4:]
        #     current_dir[directory_name] = {}
        #     current_dir = current_dir[directory_name]
        #     stack.append(current_dir)
        #     # print(value)
        elif line == "$ cd ..":
            stack.pop()
            current_dir = stack[-1]
    # print(value)
    return filesystem

def calculate_total_size(directory):
    total_size = 0
    for item in directory.values():
        if isinstance(item, int):
            total_size += item
        elif isinstance(item, dict):
            total_size += calculate_total_size(item)
    return total_size

def find_directories_within_limit(filesystem, limit):
    directories_within_limit = []
    stack = [(filesystem, "")]

    while stack:
        directory, path = stack.pop()
        total_size = calculate_total_size(directory)

        if total_size <= limit:
            directories_within_limit.append(total_size)

        for name, item in directory.items():
            if isinstance(item, dict):
                stack.append((item, f"{path}/{name}"))
        # print(stack)

    return directories_within_limit

with open("day7_data.txt", "r") as file:
    listing = file.read().split("\n")
filesystem = parse_directory_listing(listing)
directories_within_limit = find_directories_within_limit(filesystem, 100000)
sum_of_total_sizes = sum(directories_within_limit)

print(sum_of_total_sizes)

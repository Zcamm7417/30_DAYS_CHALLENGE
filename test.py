import re

def parse_directory_listing(listing):
    filesystem = {}
    current_dir = filesystem
    stack = [current_dir]
    new = []

    for dir in listing:
        dir = dir.replace("cd ", "dir ")
    #     # for line in dir:
    #         # new.append(line)
    #     # listy.append(dir)

    #     print(dir)

    for line in dir:
        if line.startswith("dir "):
            directory_name = line[4:]
            current_dir[directory_name] = {}
            current_dir = current_dir[directory_name]
            stack.append(current_dir)
        elif re.match(r"\d+ \w+", line):
            file_size, file_name = line.split()
            current_dir[file_name] = int(file_size)
            # print(file_name)
        elif line == "dir ..":
            stack.pop()
            current_dir = stack[-1]
        # elif line.startswith("cd "):
        #     line.replace("cd ", "dir ")
        #     directory_name = line[2:]
        #     current_dir = current_dir
        #     stack.append(current_dir)
        # elif line.startswith("cd "):
        #     directory = line.split()[1]
        #     if directory == "..":
        #         current_directory = "/".join(current_directory.split("/")[:-2]) + "/"
        #     else:
        #         current_directory = "/"
        #         current_directory = current_directory + directory + "/"

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
        # print(directory)

        if total_size <= limit and path != "":
            directories_within_limit.append(total_size)
            # print(total_size)
        for name, item in directory.items():
            if isinstance(item, dict):
                stack.append((item, f"{path}/{name}"))

    return directories_within_limit

with open("test7.txt", "r") as file:
    listing = file.read().split("\n")
    for dir in listing:
        dir = dir.replace("cd ", "dir ")
        # print(dir)

filesystem = parse_directory_listing(listing)
directories_within_limit = find_directories_within_limit(filesystem, 100000)
sum_of_total_sizes = sum(directories_within_limit)

print(sum_of_total_sizes)

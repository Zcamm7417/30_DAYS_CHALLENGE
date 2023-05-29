# def calculate_x(program):
#     x = 1  # Initial value of register X
#     cycle_count = 0  # Current cycle count
#     x_values = []  # List to store X values

#     for instruction in program:
#         op, *args = instruction.split()
#         if op == "addx":
#             value = int(args[0])
#             cycle_count += 2
#             x += value
#             # cycle_count += 1
#         elif op == "noop":
#             cycle_count += 1
#         if cycle_count >= 20:
#             x_values.append(x)
#             break

#     return x_values

# with open("day10_data.txt", "r") as file:
#     program = [line.strip() for line in file.readlines()]
# # Get the value of X at cycle 20
# x_values = calculate_x(program)

# # Print the value
# if x_values:
#     print(f"The value of X at cycle 20 is: {x_values[0]}")
# else:
#     print("The cycle count did not reach 20.")

def calculate_x(program):
    x = 1  # Initial value of register X
    cycle_count = 0  # Current cycle count

    for instruction in program:
        op, *args = instruction.split()
        if op == "addx":
            value = int(args[0])
            cycle_count += 2
            x += value
        elif op == "noop":
            cycle_count += 1
        if cycle_count == 20:  # Check if cycle count is exactly 20 and exclude addx instructions
            return x

    return None  # Return None if cycle count 20 is not reached or falls on an addx instruction

with open("day10_data.txt", "r") as file:
    program = [line.strip() for line in file.readlines()]
# # Get the value


# Get the value of X at cycle count 20 (excluding addx instructions)
x_value = calculate_x(program)

# Print the value
if x_value is not None:
    print(f"The value of X at cycle count 20 (excluding addx instructions) is: {x_value}")
else:
    print("The cycle count did not reach 20 or falls on an addx instruction.")

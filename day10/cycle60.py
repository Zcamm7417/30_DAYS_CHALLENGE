# def calculate_x(program):
#     x = 1  # Initial value of register X
#     cycle_count = 0  # Current cycle count

#     for instruction in program:
#         op, *args = instruction.split()
#         if op == "addx":
#             value = int(args[0])
#             cycle_count += 2
#             x += value
#         elif op == "noop":
#             cycle_count += 1
#         if cycle_count >= 60 and (cycle_count - 20) % 40 == 0 and op != "addx":
#             return x

#     return None  # Return None if cycle count 60 is not reached or falls on an addx instruction

# with open("day10_data.txt", "r") as file:
#     program = [line.strip() for line in file.readlines()]

# x_value = calculate_x(program)

# # Print the value
# if x_value is not None:
#     print(f"The value of X at cycle count 60 (excluding addx instructions) is: {x_value}")
# else:
#     print("The cycle count did not reach 60 or falls on an addx instruction.")

def calculate_x(program):
    x = 1  # Initial value of register X
    cycle_count = 0  # Current cycle count
    x_sum = 0  # Sum of x_values

    for instruction in program:
        op, *args = instruction.split()
        if op == "addx":
            value = int(args[0])
            x += value
            cycle_count += 2
            
        elif op == "noop":
            cycle_count += 1
        if cycle_count == 60 :
            x_sum += x

    return x

with open("test10.txt", "r") as file:
    program = [line.strip() for line in file.readlines()]


# Calculate the sum of x_values for cycle count 60 (excluding addx instructions)
x_sum = calculate_x(program)

# Print the sum
print(f"The sum of x_values for cycle count 60 (excluding addx instructions) is: {x_sum}")

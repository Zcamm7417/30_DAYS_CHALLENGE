def calculate_signal_strength(program, target_cycles):
    x = 1  # Initial value of register X
    cycle_count = 0  # Current cycle count
    signal_strengths = []

    while target_cycles:
        for instruction in program:
            op, *args = instruction.split()
            if op == "addx":
                value = int(args[0])
                cycle_count += 2
                x += value
            elif op == "noop":
                cycle_count += 1

            if cycle_count in target_cycles:
                signal_strength = cycle_count * x
                signal_strengths.append(signal_strength)
                target_cycles.remove(cycle_count)

    return signal_strengths



with open("test10.txt", "r") as file:
    program = [line.strip() for line in file.readlines()]

target_cycles = [20, 60, 100, 140, 180, 220]
signal_strengths = calculate_signal_strength(program, target_cycles)

# Calculate the sum of the signal strengths
sum_signal_strengths = sum(signal_strengths)

print(f"The sum of the signal strengths during the specified cycles is: {sum_signal_strengths}")






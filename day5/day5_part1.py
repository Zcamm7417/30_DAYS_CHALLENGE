# def rearrange_crates(starting_configuration, rearrangement_steps):
#     stacks = [list(stack) for stack in starting_configuration]

#     for step in rearrangement_steps:
#         step_parts = step.split()
#         source_stack = int(step_parts[1]) - 1
#         crate = stacks[source_stack].pop()
#         destination_stack = int(step_parts[4]) - 1
#         stacks[destination_stack].append(crate)

#     top_crates = [stack[-1] for stack in stacks]
#     return ''.join(top_crates)

# # Example usage
# starting_configuration = ['D', 'NC', 'ZMP']
# rearrangement_steps = [
#     'move 1 from 2 to 1',
#     'move 3 from 1 to 3',
#     'move 2 from 2 to 1',
#     'move 1 from 1 to 2'
# ]

# final_configuration = rearrange_crates(starting_configuration, rearrangement_steps)
# print("Final crate configuration:", final_configuration)


# def rearrange_crates(starting_configuration, rearrangement_steps):
#     stacks = [list(stack) for stack in starting_configuration]
#     # print(stacks)

#     for step in rearrangement_steps:
#         step_parts = step.split()
#         source_stack = int(step_parts[3]) - 1
#         crate = stacks[source_stack].pop()
#         destination_stack = int(step_parts[5]) - 1
#         stacks[destination_stack].append(crate)

#     top_crates = [stack[-1] for stack in stacks]
#     return ''.join(top_crates)

# # Example usage
# starting_configuration = ['NZ', 'DCM', 'P']
# rearrangement_steps = [
#     'move 1 from 2 to 1',
#     'move 3 from 1 to 3',
#     'move 2 from 2 to 1',
#     'move 1 from 1 to 2'
# ]

# final_configuration = rearrange_crates(starting_configuration, rearrangement_steps)
# print("Final crate configuration:", final_configuration)


def get_top_crates(initial_config, rearrangement_steps):
    stacks = initial_config.strip().split('\n')
    stacks = [list(stack.strip().split()) for stack in stacks]
    stacks = [stack[::-1] for stack in stacks]  # Reverse the order of crates in each stack

    for step in rearrangement_steps:
        _, _, _, source_stack, _, target_stack = step.split()
        source_stack = int(source_stack) - 1
        target_stack = int(target_stack) - 1
        crate = stacks[source_stack].pop()
        stacks[target_stack].append(crate)

    top_crates = [stack[-1] for stack in stacks]
    return ''.join(top_crates)

# Example usage
initial_config = """[D]
[N] [C]
[Z] [M] [P]"""
rearrangement_steps = ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]

result = get_top_crates(initial_config, rearrangement_steps)
print(result)

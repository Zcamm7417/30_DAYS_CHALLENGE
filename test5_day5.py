def rearrange_crates(starting_configuration, rearrangement_steps):
    stacks = [list(stack) for stack in starting_configuration]
    # stacks = [stack[::-1] for stack in stacks]

    for step in rearrangement_steps:
        parts = step.split()
        source_stack = int(parts[3]) -1
        destination_stack = int(parts[5]) -1
        # print(destination_stack)
        crate = stacks[source_stack].pop()
        stacks[destination_stack].append(crate)

    # top_crates = [stack[-1] for stack in stacks]
    # return ''.join(top_crates)
    top_crates = [stack[-1] if stack else ' ' for stack in stacks]
    return ''.join(top_crates)

# Example usage
starting_configuration = ['NZ', 'DCM', 'P']
# starting_configuration = ['GBDCPR', 'GVH', 'MPJDQSN', 'MNCDGLSP', 'SLFPCNBJ', 'STGVZDBQ', 'QTFHMZB', 'FBDMC', 'GQCF']

# with open("test3.txt", "r") as file:
    # rearrangement_steps = file.read().split("\n")
rearrangement_steps = [
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2'
]
final_configuration = rearrange_crates(starting_configuration, rearrangement_steps)
print("Final crate configuration:", final_configuration)
# cmz
# pdm
# dcp
# dnc
# cnm
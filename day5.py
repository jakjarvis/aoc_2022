from read_input import input_string

lines = input_string(5, 2022).split("\n")

crate_rows = []
instructions = []

for line in lines:
    if line == "":
        pass
    elif line[0] == "[":
        crate_rows += [line]
    elif line[:4] == "move":
        instructions += [line]


def set_stacks(crate_rows):
    stacks = {}
    for stack in range(int((len(crate_rows[0]) + 1) / 4)):
        stacks[stack + 1] = []
    for row_number in range(len(crate_rows) - 1, -1, -1):
        crate_row = crate_rows[row_number]
        stack = 1
        while stack <= len(stacks):
            if crate_row[1] != " ":
                stacks[stack] += crate_row[1]
            crate_row = crate_row[4:]
            stack += 1
    return stacks


def set_instructions(instructions):
    instruction_list = []
    for instruction in instructions:
        number = 0
        if instruction[6] == " ":
            number = int(instruction[5])
            instruction = instruction[7:]
        else:
            number = int(instruction[5:7])
            instruction = instruction[8:]
        stackA = int(instruction[5])
        stackB = int(instruction[10])
        instruction_list += [[number, stackA, stackB]]
    return instruction_list


def top_crates(stacks):
    top_crates = []
    for stack in range(1, len(stacks) + 1):
        top_crates += stacks[stack][-1]
    return "".join(top_crates)


def move_single_crates(stacks, instruction_list):
    for instruction in instruction_list:
        number, stackA, stackB = instruction
        for move in range(number):
            crate = stacks[stackA][-1]
            stacks[stackA].pop()
            stacks[stackB] += crate
    return top_crates(stacks)


def move_multiple_crates(stacks, instruction_list):
    for instruction in instruction_list:
        number, stackA, stackB = instruction
        stacks[stackB] += stacks[stackA][(number * (-1)) :]
        stacks[stackA] = stacks[stackA][: (number * (-1))]
    return top_crates(stacks)


part1_solution = move_single_crates(
    set_stacks(crate_rows), set_instructions(instructions)
)
part2_solution = move_multiple_crates(
    set_stacks(crate_rows), set_instructions(instructions)
)

print("Part 1 solution is: ", part1_solution, "\nPart 2 solution is: ", part2_solution)

from read_input import input_string

input_list = input_string(3, 2022).split("\n")


def find_common_char(string1, string2):
    for char1 in string1:
        for char2 in string2:
            if char1 == char2:
                return char1


def find_badge_id(trio_of_backpacks):
    common_list = []
    for char0 in trio_of_backpacks[0]:
        if char0 in [*trio_of_backpacks[1]]:
            common_list += char0
    for char2 in trio_of_backpacks[2]:
        if char2 in common_list:
            return char2


def prioritse(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


part1_solution = 0
part2_solution = 0

for backpack in input_list:
    compartment_size = int(len(backpack) / 2)
    top_compartment = backpack[:(compartment_size)]
    bottom_compartment = backpack[(compartment_size):]
    common_char = find_common_char(top_compartment, bottom_compartment)
    part1_solution += prioritse(common_char)

while len(input_list) > 0:
    badge_id = find_badge_id(input_list[:3])
    part2_solution += prioritse(badge_id)
    input_list = input_list[3:]

print("Part 1 solution is: ", part1_solution, "\nPart 2 solution is: ", part2_solution)

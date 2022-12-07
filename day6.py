from read_input import input_string

datastream_buffer = input_string(6, 2022)

for character in range(4, len(datastream_buffer) - 3):
    potential_hash = datastream_buffer[(character - 4) : character]
    if len(set(list(potential_hash))) == 4:
        part1_solution = character
        break

for character in range(14, len(datastream_buffer) - 13):
    potential_hash = datastream_buffer[(character - 14) : character]
    if len(set(list(potential_hash))) == 14:
        part2_solution = character
        break

print("Part 1 solution: ", part1_solution, "\nPart 2 solution: ", part2_solution)

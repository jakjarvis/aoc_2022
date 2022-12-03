from read_input import input_string

strings_list = input_string(1, 2022).split("\n\n")
inventories_list = []
for string in strings_list:
    inventory = string.split("\n")
    inventory_list = []
    for snack in inventory:
        inventory_list.append(int(snack))
    inventories_list += [inventory_list]

elves_dict = {}
elf = 0
for inventory in inventories_list:
    elves_dict[str(elf)] = sum(inventory)
    elf += 1

elves_list = elves_dict.values()
part1_solution = max(elves_list)

sorted_elves = sorted(elves_list, reverse=True)
part2_solution = sum(sorted_elves[:3])

print("Part 1 solution: ", part1_solution, "\nPart 2 solution: ", part2_solution)

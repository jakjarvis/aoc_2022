from read_input import input_string
import re

pairs = input_string(4, 2022).split("\n")

test_data = [
    "9-62,61-61",
]


def contained_pairs(pairs):
    solution = 0
    for pair in pairs:
        sectors = re.split("-|,", pair)
        elf1_min, elf1_max, elf2_min, elf2_max = list(map(int, sectors))
        if (
            elf1_min <= elf2_min
            and elf1_max >= elf2_max
            or elf1_min >= elf2_min
            and elf1_max <= elf2_max
        ):
            solution += 1
    return solution


def overlapping_pairs(pairs):
    solution = 0
    for pair in pairs:
        sectors = re.split("-|,", pair)
        elf1_min, elf1_max, elf2_min, elf2_max = list(map(int, sectors))
        if (
            elf1_min <= elf2_min
            and elf1_max >= elf2_min
            or elf2_min <= elf1_min
            and elf2_max >= elf1_min
        ):
            solution += 1
    return solution


print(
    "Part 1 solution: ",
    contained_pairs(pairs),
    "\nPart 2 solution: ",
    overlapping_pairs(pairs),
)

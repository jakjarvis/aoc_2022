from read_input import input_string

# Each throw has one score that is dependent on what the other person through. In part 1 this is the result of the round (win, draw lose), in part 2 this is the score from your own throw.
dependent_score_1 = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}
dependent_score_2 = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}
# Each throw has one score that is independent of your opponent, and can be calculated independently from the strategy guide. In part 1 this is the score from your own throw, in part 2 this is the score from the result.
independent_score_1 = {"X": 1, "Y": 2, "Z": 3}
independent_score_2 = {"X": 0, "Y": 3, "Z": 6}

# In both part 1 and part 2, the final score is calculated from looking up the dependent and independnent score components from the dictoinaries defined above.
def score(dependent_score, independent_score):
    score = 0
    opponent = ""
    for throw in input_string(2, 2022).split():
        if opponent == "":
            opponent = throw
        else:
            score1 = dependent_score[opponent][throw]
            score2 = independent_score[throw]
            opponent = ""
            score += score1 + score2

    return score


part1_solution = score(dependent_score_1, independent_score_1)
part2_solution = score(dependent_score_2, independent_score_2)

print("Part 1 solution is: ", part1_solution, "\nPart 2 solution is: ", part2_solution)

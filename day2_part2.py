def calculate_score(strategy_guide):
    a_value = 0
    b_value = 0
    c_value = 0
    score = 0

    for line in strategy_guide:
        # A, B, C == ROCK, PAPER, SCISCORS
        # A, B, C == 1, 2, 3
        # X, Y, Z == LOSE, DRAW, WIN
        opponent_choice, your_choice = line.split()
        if your_choice == "X":
            score += 0
        elif your_choice == "Y":
            score += 3
        elif your_choice == "Z":
            score += 6
        # for A, B, C value
        if opponent_choice == "A":
            a_value += 1
        elif opponent_choice == "B":
            b_value += 1
        elif opponent_choice == "C":
            c_value += 1

        # if opponent_choice == "A" and your_choice == "X":
        #     score +=  1
        # elif opponent_choice == "B" and your_choice == "Y":
        #     score += 4
        # elif opponent_choice == "C" and your_choice == "Z":
        #     score += 7
        # elif opponent_choice == "A" and your_choice == "Y":
        #     score += 4
        # elif opponent_choice == "A" and your_choice == "Z":
        #     score += 7
        # elif opponent_choice == "B" and your_choice == "X":
        #     score += 1
        # elif opponent_choice == "B" and your_choice == "Z":
        #     score += 7
        # elif opponent_choice == "C" and your_choice == "X":
        #     score += 1
        # elif opponent_choice == "C" and your_choice == "Y":
        #     score += 4
    total_score = score + a_value + b_value + c_value
    return total_score 
with open("day2_data.txt", "r") as file:
    strategy_guide = file.read().split("\n")

total_score = calculate_score(strategy_guide)
print(f"The total score according to the strategy guide is: {total_score}")
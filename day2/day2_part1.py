def calculate_score(strategy_guide):
    score = 0
    same_value = 0
    win_value = 0

    for line in strategy_guide:
        opponent_choice, your_choice = line.split()
        A, B, C = 1, 2, 3
        X, Y, Z = 1, 2, 3

        if your_choice == "X":
            score += 1
        elif your_choice == "Y":
            score += 2
        elif your_choice == "Z":
            score += 3
        # for same value
        if opponent_choice == "A" and your_choice == "X":
            same_value += 3
        elif opponent_choice == "B" and your_choice == "Y":
            same_value += 3
        elif opponent_choice == "C" and your_choice == "Z":
            same_value += 3
        # for your_choice win
        if opponent_choice == "C" and your_choice == "X":
            win_value += 6
        elif opponent_choice == "A" and your_choice == "Y":
            win_value += 6
        elif opponent_choice == "B" and your_choice == "Z":
            win_value += 6
    total_score = score + win_value + same_value
    return total_score 

with open("day2_data.txt", "r") as file:
    strategy_guide = file.read().split("\n")

total_score = calculate_score(strategy_guide)
print(f"The total score according to the strategy guide is: {total_score}")
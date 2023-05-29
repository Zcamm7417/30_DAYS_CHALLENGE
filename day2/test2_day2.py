def calculate_score(strategy_guide):
    score = 0

    for line in strategy_guide:
        opponent_choice, result = line.split()
        
        if result == 'X':
            score += 1
        elif result == "Y":
            score += 4
        elif result == "Z":
            score += 7


    return score

with open("day2_data.txt", "r") as file:
    strategy_guide = file.read().split("\n")
total_score = calculate_score(strategy_guide)
print(f"The total score according to the updated strategy guide is: {total_score}")

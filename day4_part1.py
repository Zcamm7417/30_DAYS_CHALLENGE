with open("day4_data.txt", "r") as datas:
    assignments = datas.read().strip().split()
    # print(assignments)
    count = 0
    for assignment in assignments:
        first, second = assignment.split(",")
        start, end = map(int, first.split("-"))
        start2, end2 = map(int,second.split("-"))
        number_set = set(range(start, end + 1))
        number_set2 = set(range(start2, end2 + 1))
        # print(number_set2)
        if number_set.issubset(number_set2) or number_set2.issubset(number_set):
            count += 1
    print(count) 

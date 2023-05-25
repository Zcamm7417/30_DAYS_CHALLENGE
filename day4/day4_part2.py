with open("day4_data.txt", "r") as datas:
    assignments = datas.read().strip().split()
    # print(assignments)
    count = 0
    for assignment in assignments:
        first, second = assignment.split(",")
        start, end = map(int, first.split("-"))
        start2, end2 = map(int,second.split("-"))

        if start <= end2 and start2 <= end:
            count += 1
    print(f"Number of overlapping assignment pairs: {count}")

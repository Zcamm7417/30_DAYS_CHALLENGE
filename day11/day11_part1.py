def calculate_monkey_business(input_data, rounds):
    monkeys = {}
    for line in input_data.split("\n"):
        if line.startswith("Monkey"):
            monkey_id = int(line.split()[1][:-1])
            monkeys[monkey_id] = {"start_items": [], "operation": "", "test": "", "if_true": "", "if_false": ""}
            continue
        elif line.startswith("Starting items"):
            monkey_items = line.split(": ")[1].split(", ")
            monkeys[monkey_id]["start_items"] = [int(item) for item in monkey_items]
        elif line.startswith("Operation"):
            monkeys[monkey_id]["operation"] = line.split(": ")[1]
        elif line.startswith("Test"):
            monkeys[monkey_id]["test"] = line.split(": ")[1]
        elif line.startswith("If true"):
            monkeys[monkey_id]["if_true"] = line.split(": ")[1]
        elif line.startswith("If false"):
            monkeys[monkey_id]["if_false"] = line.split(": ")[1]

    def apply_operation(worry_level, operation):
        namespace = {"old": worry_level}
        exec(operation, namespace)
        return namespace["new"]

    def get_throw_destination(monkey_id, worry_level, test, if_true, if_false):
        if eval(test):
            return int(if_true.split()[-1])
        else:
            return int(if_false.split()[-1])

    def calculate_round(monkeys, round_num):
        for monkey_id, monkey in monkeys.items():
            if round_num >= len(monkey["start_items"]):
                break
            items = monkey["start_items"][round_num:]

            for i, item in enumerate(items):
                worry_level = item
                worry_level = apply_operation(worry_level, monkey["operation"])
                worry_level = worry_level // 3
                monkey["start_items"].append(worry_level)
                destination = get_throw_destination(monkey_id, worry_level, monkey["test"], monkey["if_true"], monkey["if_false"])
                monkeys[destination]["start_items"].append(worry_level)

    for i in range(rounds):
        calculate_round(monkeys, i)

    monkey_counts = [len(monkey["start_items"]) for monkey in monkeys.values()]
    monkey_counts.sort(reverse=True)
    monkey_business = monkey_counts[0] * monkey_counts[1]
    return monkey_business

input_data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0
Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3
Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

rounds = 20
monkey_business = calculate_monkey_business(input_data, rounds)
print(f"The level of monkey business after {rounds} rounds is: {monkey_business}")

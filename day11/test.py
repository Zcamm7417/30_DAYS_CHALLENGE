# Define the monkeys and their attributes
monkeys = {
    0: {
        "starting_items": [79, 98],
        "operation": lambda x: x * 19,
        "test": lambda x: x % 23 == 0,
        "if_true": 2,
        "if_false": 3,
        "inspection_count": 0
    },
    1: {
        "starting_items": [54, 65, 75, 74],
        "operation": lambda x: x + 6,
        "test": lambda x: x % 19 == 0,
        "if_true": 2,
        "if_false": 0,
        "inspection_count": 0
    },
    2: {
        "starting_items": [79, 60, 97],
        "operation": lambda x: x * x,
        "test": lambda x: x % 13 == 0,
        "if_true": 1,
        "if_false": 3,
        "inspection_count": 0
    },
    3: {
        "starting_items": [74],
        "operation": lambda x: x + 3,
        "test": lambda x: x % 17 == 0,
        "if_true": 1,
        "if_false": 0,
        "inspection_count": 0
    }
}

# Simulate 20 rounds of stuff-slinging
for _ in range(20):
    for monkey in monkeys.values():
        items_to_throw = []

        for item in monkey["starting_items"]:
            # Inspect the item
            worry_level = item
            worry_level = monkey["operation"](worry_level)
            worry_level = worry_level // 3

            # Update inspection count for the current monkey
            monkey["inspection_count"] += 1

            # Test the worry level and decide where to throw the item
            if monkey["test"](worry_level):
                recipient_monkey = monkey["if_true"]
            else:
                recipient_monkey = monkey["if_false"]

            items_to_throw.append((worry_level, recipient_monkey))

        # Clear the starting items list for the current monkey
        monkey["starting_items"] = []

        # Throw the items to the recipient monkeys
        for item, recipient_monkey in items_to_throw:
            monkeys[recipient_monkey]["starting_items"].append(item)

# Find the two most active monkeys
sorted_monkeys = sorted(monkeys.values(), key=lambda x: x["inspection_count"], reverse=True)
most_active_monkeys = sorted_monkeys[:2]

# Calculate the level of monkey business
monkey_business_level = most_active_monkeys[0]["inspection_count"] * most_active_monkeys[1]["inspection_count"]

# Output the level of monkey business
print("The level of monkey business after 20 rounds of stuff-slinging is:", monkey_business_level)

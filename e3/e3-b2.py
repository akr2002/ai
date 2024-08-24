# Define the rules
rules = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}

# Define the goal
goal = "A"


# Backward chaining function
def backward_chaining(goal, rules, facts=None):
    if facts is None:
        facts = []
    if goal in facts:
        return True
    if goal not in rules:
        return False
    for rule in rules[goal]:
        if not backward_chaining(rule, rules, facts):
            return False
    facts.append(goal)
    return True


# Run backward chaining
if backward_chaining(goal, rules):
    print("Goal achieved!")
else:
    print("Goal not achieved.")

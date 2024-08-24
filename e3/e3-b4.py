class Fact:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent

    def is_satisfied(self, facts):
        for antecedent in self.antecedents:
            if (
                antecedent.name not in facts
                or facts[antecedent.name] != antecedent.value
            ):
                return False
        return True


def find_solution(goal, facts, rules):
    stack = [(goal, [goal])]

    while stack:
        current_goal, path = stack.pop()
        for rule in rules:
            if rule.consequent and rule.consequent[0].name == current_goal:
                if rule.is_satisfied(facts):
                    new_path = path + [
                        rule.antecedents[0].name for antecedent in rule.antecedents
                    ]
                    if rule.consequent[0].name not in path:
                        stack.append((current_goal, new_path))


def backward_chaining(goal, facts, rules):
    solution = find_solution(goal, facts, rules)
    if solution:
        print(solution)
    else:
        print("No solution found.")


# Define facts
facts = {
    Fact("is_human", True),
    Fact("is_male", False),
    Fact("is_mammal", True),
    Fact("is_man", True),
}

# Define rules
rules = [
    Rule([Fact("is_human", True)], [Fact("is_mammal", True)]),
    Rule([Fact("is_mammal", True), Fact("is_male", True)], [Fact("is_man", True)]),
]

# Run backward chaining
backward_chaining("is_man", facts, rules)

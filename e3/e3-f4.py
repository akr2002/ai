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


def apply_rule(rule, facts):
    if rule.is_satisfied(facts):
        for fact in rule.consequent:
            if fact.name not in facts:
                facts[fact.name] = True


def forward_chaining(rules, facts):
    for rule in rules:
        apply_rule(rule, facts)


# Define facts
facts = {Fact("is_human", True), Fact("is_male", False)}

# Define rules
rules = [
    Rule([Fact("is_human", True)], [Fact("is_mammal", True)]),
    Rule([Fact("is_mammal", True), Fact("is_male", True)], [Fact("is_man", True)]),
]

# Run forward chaining
forward_chaining(rules, facts)

# Print the resulting facts
for fact in facts:
    print(fact.name)

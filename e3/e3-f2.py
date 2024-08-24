# Define the rules
rules = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}

# Define the facts
facts = ["A"]


# Forward chaining function
def forward_chaining(facts, rules):
    for fact in facts:
        if fact in rules:
            for rule in rules[fact]:
                if rule not in facts:
                    facts.append(rule)
                    forward_chaining([rule], rules)


# Run forward chaining
forward_chaining(facts, rules)

# Print the results
print("Final facts:", facts)

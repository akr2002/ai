class Rule:
    def __init__(self, consequent, antecedent):
        self.consequent = consequent
        self.antecedent = antecedent

    def is_applicable(self, knowledge_base):
        return all(fact in knowledge_base for fact in self.consequent)

    def apply(self, knowledge_base):
        if self.is_applicable(knowledge_base):
            knowledge_base.update(self.antecedent)
            return True
        return False


class KnowledgeBase:
    def __init__(self, facts):
        self.facts = set(facts)

    def update(self, new_facts):
        self.facts.update(new_facts)

    def __contains__(self, fact):
        return fact in self.facts


def backward_chaining(knowledge_base, rules, goal):
    if goal in knowledge_base:
        return True

    for rule in rules:
        if rule.consequent == goal:
            antecedents = rule.antecedent
            if all(
                backward_chaining(knowledge_base, rules, antecedent)
                for antecedent in antecedents
            ):
                return True

    return False


# Example usage
if __name__ == "__main__":
    # Define facts
    facts = ["cat(fluffy)", "mammal(cat)"]

    # Define rules
    rules = [
        Rule(["mammal(X)", "has_fur(X)"], ["warm_blooded(X)"]),
        Rule(["cat(X)"], ["mammal(X)", "has_fur(X)"]),
        Rule(["warm_blooded(X)"], ["can_regulate_body_temp(X)"]),
    ]

    # Create knowledge base
    kb = KnowledgeBase(facts)

    # Define goal
    goal = "can_regulate_body_temp(fluffy)"

    # Apply backward chaining
    result = backward_chaining(kb, rules, goal)

    # Print result
    print("Goal is achievable:", result)

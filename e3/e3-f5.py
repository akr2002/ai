class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def is_applicable(self, knowledge_base):
        return all(fact in knowledge_base for fact in self.antecedent)

    def apply(self, knowledge_base):
        if self.is_applicable(knowledge_base):
            knowledge_base.update(self.consequent)
            return True
        return False


class KnowledgeBase:
    def __init__(self, facts):
        self.facts = set(facts)

    def update(self, new_facts):
        self.facts.update(new_facts)

    def __contains__(self, fact):
        return fact in self.facts


def forward_chaining(knowledge_base, rules):
    new_facts_added = True
    while new_facts_added:
        new_facts_added = False
        for rule in rules:
            if rule.apply(knowledge_base):
                new_facts_added = True


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

    # Apply forward chaining
    forward_chaining(kb, rules)

    # Print inferred facts
    print("Inferred facts:", kb.facts)

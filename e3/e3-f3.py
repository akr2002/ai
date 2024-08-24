class Rule:
    """Represents a rule in the knowledge base."""

    def __init__(self, antecedent, consequent):
        """
        Initializes a rule.

        Args:
            antecedent (list): A list of facts that must be true for the rule to be applied.
            consequent (str): The fact that is derived when the rule is applied.
        """
        self.antecedent = antecedent
        self.consequent = consequent


class KnowledgeBase:
    """Represents the knowledge base of the expert system."""

    def __init__(self):
        """
        Initializes an empty knowledge base.
        """
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        """
        Adds a fact to the knowledge base.

        Args:
            fact (str): The fact to add.
        """
        self.facts.add(fact)

    def add_rule(self, rule):
        """
        Adds a rule to the knowledge base.

        Args:
            rule (Rule): The rule to add.
        """
        self.rules.append(rule)

    def forward_chaining(self):
        """
        Applies forward chaining to the knowledge base.

        Returns:
            set: The set of derived facts.
        """
        derived_facts = set()
        while True:
            new_facts = set()
            for rule in self.rules:
                if all(antecedent in self.facts for antecedent in rule.antecedent):
                    new_facts.add(rule.consequent)
            if new_facts.issubset(derived_facts):
                break
            derived_facts.update(new_facts)
            self.facts.update(new_facts)
        return derived_facts


# Example usage
kb = KnowledgeBase()

# Add facts
kb.add_fact("It is raining.")
kb.add_fact("The road is slippery.")

# Add rules
kb.add_rule(Rule(["It is raining.", "The road is slippery."], "The road is dangerous."))
kb.add_rule(Rule(["The road is dangerous."], "You should drive carefully."))

# Apply forward chaining
derived_facts = kb.forward_chaining()
print("Derived Facts:")
for fact in derived_facts:
    print(fact)

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

    def backward_chaining(self, goal):
        """
        Applies backward chaining to the knowledge base to prove a goal.

        Args:
            goal (str): The goal to prove.

        Returns:
            bool: True if the goal is proven, False otherwise.
        """
        if goal in self.facts:
            return True
        for rule in self.rules:
            if rule.consequent == goal:
                if all(
                    self.backward_chaining(antecedent) for antecedent in rule.antecedent
                ):
                    return True
        return False


# Example usage
kb = KnowledgeBase()

# Add facts
kb.add_fact("It is raining.")
kb.add_fact("The road is slippery.")

# Add rules
kb.add_rule(Rule(["It is raining.", "The road is slippery."], "The road is dangerous."))
kb.add_rule(Rule(["The road is dangerous."], "You should drive carefully."))

# Apply backward chaining
goal = "You should drive carefully."
if kb.backward_chaining(goal):
    print(f"The goal '{goal}' is proven.")
else:
    print(f"The goal '{goal}' is not proven.")

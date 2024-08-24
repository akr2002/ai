class KnowledgeBase:
    def __init__(self):
        self.rules = []
        self.facts = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact):
        self.facts.append(fact)

    def backward_chaining(self, goal):
        # If the goal is already in the facts, return True
        if goal in self.facts:
            return True

        # Search for rules that conclude the goal
        for rule in self.rules:
            if rule["conclusion"] == goal:
                # Recursively check if all premises are satisfied
                premises_satisfied = True
                for premise in rule["premises"]:
                    if not self.backward_chaining(premise):
                        premises_satisfied = False
                        break

                if premises_satisfied:
                    # If all premises are satisfied, add the goal to the facts
                    self.facts.append(goal)
                    return True

        # If no rules can satisfy the goal, return False
        return False


# Example usage:
kb = KnowledgeBase()

# Add facts
kb.add_fact("A")
kb.add_fact("B")

# Add rules (premises -> conclusion)
kb.add_rule({"premises": ["A", "B"], "conclusion": "C"})
kb.add_rule({"premises": ["C"], "conclusion": "D"})

# Try to prove goal D
goal = "D"
if kb.backward_chaining(goal):
    print(f"Goal '{goal}' is proved.")
else:
    print(f"Goal '{goal}' cannot be proved.")

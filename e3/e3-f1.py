class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, condition, consequence):
        self.rules.append((condition, consequence))

    def infer(self):
        inferred = True
        while inferred:
            inferred = False
            for condition, consequence in self.rules:
                if condition.issubset(self.facts) and consequence not in self.facts:
                    self.facts.add(consequence)
                    inferred = True
                    print(f"Inferred: {consequence}")


# Example Usage
if __name__ == "__main__":
    kb = KnowledgeBase()

    # Adding initial facts
    kb.add_fact("rainy")
    kb.add_fact("weekday")

    # Adding rules
    kb.add_rule({"rainy"}, "carry_umbrella")
    kb.add_rule({"weekday", "rainy"}, "drive_to_work")
    kb.add_rule({"sunny"}, "go_for_a_walk")

    # Inference
    print("Initial Facts:", kb.facts)
    kb.infer()
    print("Final Facts:", kb.facts)

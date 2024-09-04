class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = []
        self.inferences = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact):
        self.facts.append(fact)

    def infer(self):
        for rule in self.rules:
            if all(fact in self.facts for fact in rule["conditions"]):
                self.inferences.append(rule["conclusion"])

    def get_inferences(self):
        return self.inferences


# Define the rules
rule1 = {"conditions": ["fever", "cough"], "conclusion": "flu"}

rule2 = {"conditions": ["sore throat", "fever"], "conclusion": "strep throat"}

rule3 = {"conditions": ["headache", "stiff neck"], "conclusion": "meningitis"}

# Create an expert system instance
system = ExpertSystem()

# Add rules to the system
system.add_rule(rule1)
system.add_rule(rule2)
system.add_rule(rule3)

# Add facts (symptoms provided by the user)
system.add_fact("fever")
system.add_fact("cough")

# Perform inference
system.infer()

# Output the conclusions
inferences = system.get_inferences()
print("Inferred Diagnoses:")
for inference in inferences:
    print(inference)

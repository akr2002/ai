class KripkeStructure:
    def __init__(self, states, transition_relation, labeling_function):
        self.states = states  # set of states S
        self.transition_relation = transition_relation  # transition relation R
        self.labeling_function = labeling_function  # labeling function L

    def get_successors(self, state):
        """Return the successors of a given state."""
        return [s for s in self.states if (state, s) in self.transition_relation]


def evaluate_formula(kripke_structure, formula, state):
    """Evaluate a temporal logic formula on a Kripke structure starting from a given state."""
    if isinstance(formula, str):
        # Base case: atomic proposition
        return formula in kripke_structure.labeling_function[state]

    op = formula[0]

    if op == "X":  # Next state
        next_state = kripke_structure.get_successors(state)
        if not next_state:
            return False  # No successor, so next state does not exist
        return evaluate_formula(kripke_structure, formula[1], next_state[0])

    elif op == "F":  # Eventually
        to_check = [state]
        checked = set()
        while to_check:
            current = to_check.pop()
            if current in checked:
                continue
            checked.add(current)
            if evaluate_formula(kripke_structure, formula[1], current):
                return True
            to_check.extend(kripke_structure.get_successors(current))
        return False

    elif op == "G":  # Globally
        to_check = [state]
        checked = set()
        while to_check:
            current = to_check.pop()
            if current in checked:
                continue
            checked.add(current)
            if not evaluate_formula(kripke_structure, formula[1], current):
                return False
            to_check.extend(kripke_structure.get_successors(current))
        return True

    elif op == "U":  # Until
        left_formula = formula[1]
        right_formula = formula[2]
        to_check = [state]
        checked = set()
        while to_check:
            current = to_check.pop()
            if current in checked:
                continue
            checked.add(current)
            if evaluate_formula(kripke_structure, right_formula, current):
                return True
            if not evaluate_formula(kripke_structure, left_formula, current):
                return False
            to_check.extend(kripke_structure.get_successors(current))
        return False

    return False


# Example usage

# Define a simple Kripke Structure
states = {"s0", "s1", "s2"}
transition_relation = {("s0", "s1"), ("s1", "s0"), ("s2", "s0")}
labeling_function = {"s0": {"p"}, "s1": {"q"}, "s2": {"r"}}

kripke_structure = KripkeStructure(states, transition_relation, labeling_function)

# Define a simple LTL formula
formula = ("U", "p", ("F", "q"))  # p U Fq

# Check if the formula holds in the initial state s0
result = evaluate_formula(kripke_structure, formula, "s2")

print(f"Does the formula hold in the initial state? {result}")

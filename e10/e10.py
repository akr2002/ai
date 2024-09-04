import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Step 1: Define Fuzzy Variables
error = ctrl.Antecedent(np.arange(-10, 11, 1), "error")
delta_error = ctrl.Antecedent(np.arange(-5, 6, 1), "delta_error")
output = ctrl.Consequent(np.arange(0, 11, 1), "output")

# Step 2: Define Membership Functions
error["negative"] = fuzz.trimf(error.universe, [-10, -10, 0])
error["zero"] = fuzz.trimf(error.universe, [-10, 0, 10])
error["positive"] = fuzz.trimf(error.universe, [0, 10, 10])

delta_error["negative"] = fuzz.trimf(delta_error.universe, [-5, -5, 0])
delta_error["zero"] = fuzz.trimf(delta_error.universe, [-5, 0, 5])
delta_error["positive"] = fuzz.trimf(delta_error.universe, [0, 5, 5])

output["low"] = fuzz.trimf(output.universe, [0, 0, 5])
output["medium"] = fuzz.trimf(output.universe, [0, 5, 10])
output["high"] = fuzz.trimf(output.universe, [5, 10, 10])

# Step 3: Define Fuzzy Rules
rule1 = ctrl.Rule(error["negative"] & delta_error["negative"], output["high"])
rule2 = ctrl.Rule(error["negative"] & delta_error["zero"], output["high"])
rule3 = ctrl.Rule(error["negative"] & delta_error["positive"], output["medium"])

rule4 = ctrl.Rule(error["zero"] & delta_error["negative"], output["high"])
rule5 = ctrl.Rule(error["zero"] & delta_error["zero"], output["medium"])
rule6 = ctrl.Rule(error["zero"] & delta_error["positive"], output["low"])

rule7 = ctrl.Rule(error["positive"] & delta_error["negative"], output["medium"])
rule8 = ctrl.Rule(error["positive"] & delta_error["zero"], output["low"])
rule9 = ctrl.Rule(error["positive"] & delta_error["positive"], output["low"])

# Step 4: Create the Control System
temperature_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]
)
temperature_simulation = ctrl.ControlSystemSimulation(temperature_ctrl)

# Step 5: Simulate the Fuzzy Controller with Different Parameters

# Example 1: Room is much colder and temperature is dropping
temperature_simulation.input["error"] = -7
temperature_simulation.input["delta_error"] = -2
temperature_simulation.compute()
output1 = temperature_simulation.output["output"]

# Example 2: Room is warmer and temperature is rising
temperature_simulation.input["error"] = 4
temperature_simulation.input["delta_error"] = 3
temperature_simulation.compute()
output2 = temperature_simulation.output["output"]

# Example 3: Room is at desired temperature and stable
temperature_simulation.input["error"] = 0
temperature_simulation.input["delta_error"] = 0
temperature_simulation.compute()
output3 = temperature_simulation.output["output"]

# Print the results
print(f"Simulation 1 - Heater power output: {output1:.2f}")
print(f"Simulation 2 - Heater power output: {output2:.2f}")
print(f"Simulation 3 - Heater power output: {output3:.2f}")

# Get the result

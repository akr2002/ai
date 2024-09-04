from collections import defaultdict


class MapColoring:
    def __init__(self, regions, neighbors, colors):
        self.regions = regions
        self.neighbors = neighbors
        self.colors = colors
        self.assignment = {}
        self.domains = {region: list(colors) for region in regions}

    def select_unassigned_variable(self):
        # Heuristic: Choose the variable with the fewest legal values (MRV)
        unassigned = [
            region for region in self.regions if region not in self.assignment
        ]
        return min(unassigned, key=lambda region: len(self.domains[region]))

    def is_consistent(self, region, color):
        for neighbor in self.neighbors[region]:
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True

    def assign(self, region, color):
        self.assignment[region] = color

    def unassign(self, region):
        if region in self.assignment:
            del self.assignment[region]

    def forward_checking(self, region, color):
        # Remove the color from the domains of all neighbors
        for neighbor in self.neighbors[region]:
            if color in self.domains[neighbor]:
                self.domains[neighbor].remove(color)

    def restore_domains(self, region, color):
        for neighbor in self.neighbors[region]:
            if color not in self.domains[neighbor]:
                self.domains[neighbor].append(color)

    def backtrack(self):
        # Check if assignment is complete
        if len(self.assignment) == len(self.regions):
            return True

        # Select unassigned variable
        region = self.select_unassigned_variable()

        # Try each color in the domain
        for color in self.domains[region]:
            if self.is_consistent(region, color):
                self.assign(region, color)
                self.forward_checking(region, color)

                # Recursive call to continue the search
                if self.backtrack():
                    return True

                # Backtrack
                self.restore_domains(region, color)
                self.unassign(region)

        return False

    def solve(self):
        if self.backtrack():
            return self.assignment
        else:
            return None


# Example usage
regions = ["A", "B", "C", "D", "E"]
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"],
}
colors = ["Red", "Green", "Blue"]

map_coloring = MapColoring(regions, neighbors, colors)
solution = map_coloring.solve()

if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution exists.")

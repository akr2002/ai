import random

# Parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
MAX_GENERATIONS = 1000


# Generate initial population
def generate_individual():
    return [random.randint(0, 7) for _ in range(8)]


def generate_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]


# Fitness function
def fitness(individual):
    clashes = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if individual[i] == individual[j]:  # Same row
                clashes += 1
            if abs(individual[i] - individual[j]) == abs(i - j):  # Same diagonal
                clashes += 1
    return 28 - clashes  # 28 is the maximum number of non-attacking pairs


# Selection
def selection(population):
    population_fitness = [
        (individual, fitness(individual)) for individual in population
    ]
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    return [individual for individual, _ in population_fitness[: POPULATION_SIZE // 2]]


# Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(0, 7)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


# Mutation
def mutate(individual):
    if random.random() < MUTATION_RATE:
        mutate_point = random.randint(0, 7)
        individual[mutate_point] = random.randint(0, 7)
    return individual


# Genetic Algorithm
def genetic_algorithm():
    population = generate_population()
    for generation in range(MAX_GENERATIONS):
        population = selection(population)
        next_generation = []
        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = random.sample(population, 2)
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1))
            next_generation.append(mutate(child2))
        population = next_generation

        # Check if we have found a solution
        for individual in population:
            if fitness(individual) == 28:
                print(f"Solution found in generation {generation}: {individual}")
                return individual

    print("No solution found")
    return None


# Run the Genetic Algorithm
solution = genetic_algorithm()

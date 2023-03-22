from deap import base, algorithms
from deap import creator
from deap import tools

import random
import matplotlib.pyplot as plt
import numpy as np
import time

start = time.time()

dim = 20  # Dimenshion of problem
maxFitness = dim * (dim - 1) / 2

POPULATION_SIZE = 100  # The number of individuals in population
P_CROSSOVER = 1.0  # Probability for crossover
P_MUTATION = 1.0  # Probability per mutation for the individual
MAX_GENERATIONS = 2500  # Max nember of generations
indpb = 0.035  # Probability per mutation for the gene
tourn_size = 2  # Tournament size

RANDOM_SEED = None

random.seed(RANDOM_SEED)

# Class "FitnessMax" that is inherited from base.Fitness, attribute - weights=(1.0,) because it needs to maximise the fitness_function
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Class "Individual" that is inherited from list, attribute - "FitnessMax"
creator.create("Individual", list, fitness=creator.FitnessMax)


def fitness(chromosome):
    # Calculate collisions in horizontal direction
    horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2
    diagonal_collisions = 0

    n = len(chromosome)

    # Calculate collisions in right and left directions
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    # Add right and left collisions to the diagonal_collisions
    diagonal_collisions = 0
    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter

        # Return fitness
    return int(maxFitness - (horizontal_collisions + diagonal_collisions)),


toolbox = base.Toolbox()

# Create gene in span between 1 and n
toolbox.register("Gene_creator", random.randint, 1, dim)

# Create individual - "individualCreator" puts n's genes from "Gene_creator" in Individual - list
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.Gene_creator, dim)

# Create list of Individuals with number equal to POPULATION_SIZE
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator, POPULATION_SIZE)

# Implemenation of population
population = toolbox.populationCreator()

# Implementation of evaluation
toolbox.register("evaluate", fitness)

# Implementation of selection with tourn_size
toolbox.register("select", tools.selTournament, tournsize=tourn_size)

# Implementation of crossover with tourn_size
toolbox.register("mate", tools.cxOnePoint)

# Implementation of mutation with indpb parameter
toolbox.register("mutate", tools.mutUniformInt, low=1, up=dim, indpb=indpb)

# Parameters for graphics
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("max", np.max)
stats.register("avg", np.mean)
stats.register("min", np.min)

# Genetic algorithm with all of operators that were created earlier
population, logbook = algorithms.eaSimple(population, toolbox,
                                          cxpb=P_CROSSOVER,
                                          mutpb=P_MUTATION,
                                          ngen=MAX_GENERATIONS,
                                          stats=stats,
                                          verbose=True)

# Showing the graphics
maxFitnessValues, meanFitnessValues, minFitnessValues = logbook.select("max", "avg", "min")

print('MaxFitness - ', maxFitness)
fig, ax = plt.subplots()
maxFitness, = ax.plot(maxFitnessValues, label="maxFitness")
minFitness, = ax.plot(minFitnessValues, label="minFitness")
meanFitness, = ax.plot(meanFitnessValues, label="meanFitness")

plt.xlabel('Generation')
plt.ylabel('Maximum, average and minimum fitness')
plt.title('Dependence of the maximum, average and minimum fitness on the generation')

fig.legend(loc='outside center right')
plt.show()

end = time.time()
print("Time for algorithm: ", end - start)

for chromosome in population:
  if chromosome.fitness.wvalues == maxFitnessValues[-1]:

    a = np.array(chromosome)
    b = np.zeros((a.size, a.max()))
    b[np.arange(a.size), a - 1] = 1
    b = np.rot90(b, k=1)
    print(b)

    break

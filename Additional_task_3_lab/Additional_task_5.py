from deap import base, algorithms
from deap import creator
from deap import tools

import random, math
import matplotlib.pyplot as plt
import numpy as np
import time

start = time.time()

dim = 3  # Dimension of problem

POPULATION_SIZE = 100  # The number of individuals in population
P_CROSSOVER = 1.0  # Probability for crossover
P_MUTATION = 1.0  # Probability per mutation for the individual
MAX_GENERATIONS = 2000  # Max number of generations
indpb = 0.075  # Probability per mutation for the gene
tourn_size = 30  # Tournament size

RANDOM_SEED = None

random.seed(RANDOM_SEED)

# Class "FitnessMax" that is inherited from base.Fitness, attribute - weights=(-1.0,) because it needs to minimize the fitness function
creator.create("FitnessMax", base.Fitness, weights=(-1.0,))

# Class "Individual" that is inherited from list, attribute - "FitnessMax"
creator.create("Individual", list, fitness=creator.FitnessMax)


def fitness(x):

    """
    :param x: individual in population
    :return: fitness value
    """
    total = 0
    for i in range(len(x)-1):
	    total += 100*math.pow((x[i+1] - math.pow(x[i],2)),2) + math.pow((x[i]-1),2)

    return total,

toolbox = base.Toolbox()

# Create gene in span between -2.048 and 2.048
toolbox.register("Gene_creator", random.uniform, -2.048, 2.048)

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

# Implementation of crossover
toolbox.register("mate", tools.cxUniform, indpb=0.5)

# Implementation of mutation with indpb parameter
toolbox.register("mutate", tools.mutUniformInt, low=-2, up=2, indpb=indpb)

# Parameters for graphics
stats = tools.Statistics(key=lambda ind: ind.fitness.values)

stats.register("min", np.min)

# Genetic algorithm with all operators that were created earlier
population, logbook = algorithms.eaSimple(population, toolbox,
                                          cxpb=P_CROSSOVER,
                                          mutpb=P_MUTATION,
                                          ngen=MAX_GENERATIONS,
                                          stats=stats,
                                          verbose=True)

end = time.time()
print("Time for algorithm: ", end - start, "c")

# Showing the graphics
minFitnessValues = logbook.select("min")

print('OptimalFitness - ', 0)
fig, ax = plt.subplots()

minFitness, = ax.plot(minFitnessValues, label="minFitness")


plt.xlabel('Generation')
plt.ylabel('Minimum fitness')
plt.title('Dependence on the minimum fitness on the generation')

fig.legend(loc='outside center right')
plt.show()


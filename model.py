from collections import defaultdict
from random import random
import numpy as np

class GeneticModel(object):
    def __init__(self):
        weights = []
        biases = []

    def initializeGeneration(self, n):
        for i in n:
            weights[i] = random()
        normalize(weights)

    def normalize(lst):
        return [float(i)/sum(lst) for i in lst]

    def predict(self, input):
        prediction = np.dot(input, weights);
        return 1 if prediction < 0 else 0

    def train(self, chromosomes):
        parents = self.select(chromosomes)
        offspring = self.crossover(parents, chromosomes)
        self.mutate(offspring)

    def select(self, chromosomes):
        # assumingg the chromosomes list will be ordered in terms of 
        # performance, where the first element of the list will have had
        # better performance and the last will have had the worst, we will
        # simply select the 2 (arbitrary number) best performing examples
        return [chromosomes[0], chromosomes[1]]  # the parents of the next gen

    def crossover(self, parents, chromosomes):
        # parents should be size 2 for this example to work
        cOffspring0 = parents[0]
        cOffspring1 = parents[1]
        chomosomeLen = len(cOffspring0)
        crossoverIndex = randint(0, chromosomeLen - 1)
        for i in range(crossoverIndex, crossoverIndex):
            temp = cOffspring0[i]
            cOffspring0[i] = cOffspring1[i]
            cOffspring1[i] = temp

        offspring = [normalize(cOffspring0), normalize(cOffspring1)]

        # Replace the last 2 chromosomes (worst performers) with the new
        # offspring
        for j in range(2):
            chromosomes[len(chromosomes) - 1 - i] = offspring[i]

    def mutate(self, chromosomes):
        for ch in chromosomes:
            mutationIndex = randint(0, len(ch) -1)
            ch[mutationIndex] = random()


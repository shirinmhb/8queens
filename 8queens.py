import random

#initialization:
def initializePopulation(numOfqueens, numPopultion):
  population = []
  for i in range(numPopultion):
    population.append(random.sample(range(1, numOfqueens+1), numOfqueens))
  return population

def parentSelection(population):
  random5parents = []
  indexList = list(range(len(population)))
  for i in range(5):
    selectedIndex = random.choice(indexList)
    random5parents.append(population[selectedIndex])
    indexList.remove(selectedIndex)

  parentFitenss = []
  for i in range(5):
    parentFitenss.append((random5parents[i], fitness(random5parents[i])))
  parentFitenss.sort(key=lambda tup: tup[1])
  return (parentFitenss[0][0], parentFitenss[1][0])

def fitness(pheno):
  fitnessInvers = 0
  for i in range(len(pheno)):
    for j in range(len(pheno)):
      if (abs(pheno[i] - pheno[j]) == abs(i - j) and i != j):
        fitnessInvers += 1
  return fitnessInvers

def crossOver(parents):
  crossOverPoint = random.randint(1, 7)
  child = []
  for i in range (0,2):
    child.append( parents[i][:crossOverPoint] )
    oppositParentIndex = 1 - i
    for j in range(crossOverPoint, 8):
      if (parents[oppositParentIndex][j] not in child[i]):
        child[i].append(parents[oppositParentIndex][j])

    child[i] + parents[oppositParentIndex][:crossOverPoint]
    for k in range(crossOverPoint):
      el = parents[oppositParentIndex][:crossOverPoint][k]
      if (el not in child[i]):
        child[i].append(el)
  return (child)

def mutation(child):
  i = random.randint(0, 7)
  j = random.randint(0, 7)
  child[i], child[j] = child[j], child[i]

def survivorSelection(newPopulation, numPopultion):
  phenoFitness = []
  for i in range(len(newPopulation)):
    phenoFitness.append((newPopulation[i], fitness(newPopulation[i])))
  phenoFitness.sort(key=lambda tup: tup[1])
  populationSurvivor = []
  for item in phenoFitness[:numPopultion]:
    populationSurvivor.append(item[0])
  return populationSurvivor

def main():
  population = initializePopulation(8, 100)
  iterations = 0
  while True:
    if (iterations >= 1000):
      print ("no solution found with 1000 iterations")
      return population
    iterations += 1
    children = crossOver(parentSelection(population))
    for child in children:
      mutationProbability = random.uniform(0.0, 1.0)
      if (mutationProbability>= 0.2):
        mutation(child)
    population.extend(children)
    survivorPopulation = (survivorSelection(population, 100))
    if (fitness(survivorPopulation[0]) == 0):
      print ("the solution is", survivorPopulation[0], "with", iterations, "iterations") 
      return population 
    else:
      population = survivorPopulation

print ("final generation", main())
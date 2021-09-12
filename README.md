# 8queens
Genetic algorithm to solve 8 queens problem

representation: permutation of 8 numbers
data structure: list
list element value: queens row position - list element index: queens column position
fitness: inverse sum of each queens penalty
population: 100 fixed
initialization: 100 random permutation of 1-8
mutation: swapping values of two randomly chosen positions
mutation probability 80%
cross over: select random crossover point, copy first parts of each parent to children, and for second parts of each child insert values from opposite parent
parent selection: select 5 parents randomly, choose the two fittest to do cross over
survivor selection: sort whole population in order by increasing inverse fitness, select the top 100 for new generation
termination condition: if reverse fitness of a phenotype is equal to 0(solution found) or if we pass 1000 iteration(no solution found)

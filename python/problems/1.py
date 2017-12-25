'''
https://projecteuler.net/problem=1
Multiples of 3 and 5
'''

ARGS = 1000

# ~0.07ms
def attempt1(upperbound):
    threes = set(range(0, upperbound, 3))
    fives = set(range(0, upperbound, 5))
    combo = threes.union(fives)
    return sum(combo)

# ~0.15ms
def attempt2(upperbound):
    return sum([x for x in range(1,upperbound,1) if x%3 == 0 or x%5 == 0])

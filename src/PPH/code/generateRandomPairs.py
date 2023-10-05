import random

def generateRandomPairs(N):
    pairs = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(N)]
    return pairs

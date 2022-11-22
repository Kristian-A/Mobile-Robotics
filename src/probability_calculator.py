import numpy as np

SQRT_TWO_PI = np.sqrt(2 * np.pi)
SQRT_SIX = np.sqrt(6)

class ProbabilityUtility:
    def bayes(likelihood, prior, evidence):
        return prior * likelihood / evidence
    
    def gaussian(x, std):
        return np.exp(-0.5 * (x / std)**2) / (std * SQRT_TWO_PI) 

    def triangular(x, std): 
        second_term = (SQRT_SIX * std - np.abs(x))/(6 * std**2)
        return np.maximum(0.0, second_term)

class MarginalSpace:
    def __init__(self):
        self.events = []

    def add_conditional_probability(self, conditional_term, prior_term):
        self.events.append(conditional_term * prior_term)

    def get_probabilities(self):
        normalization = sum(self.events)
        return list(map(lambda event: event / normalization, self.events))

class State:
    def __init__(self, probability):
        self.probability = probability
        self.conditionals = {}

    def given_previous_was(self, state, probability):
        self.conditionals[state] = probability

    def estimate(self):
        total = 0
        for state, probability in self.conditionals.items():
            total += state.probability * probability
        return total
class ProbabilityUtility:
    def bayes(likelihood, prior, evidence):
        return prior * likelihood / evidence
    
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

# P(state=clean | u, state=dirty) = 0.8, P(state = dirty) = 0.6
# P(state=clean | u, state=clean) = 1.0, P(state = clean) = 0.4
# P(state=clean | u) = P(state=clean | u, state=dirty) *  P(state = dirty) + P(state=clean | u, state=clean) * P(state = clean)
# P(state=clean | u) = 0.8 * 0.6 + 1.0 * 0.4
clean = State(0.4)
dirty = State(0.6)
# The probability of clean given previous was dirty is 0.8
clean.given_previous_was(dirty, 0.8)
clean.given_previous_was(clean, 1)
print(clean.estimate())

# Bayes Theorem Solver:
# P(x|y) = P(y|x_1)P(x_1) / (p(y|x_1)*p(x_1) + p(y|x_2)p(x_2))
marginal_space = MarginalSpace()
marginal_space_element1 = marginal_space.add_conditional_probability(0.7, 0.2)
marginal_space_element2 = marginal_space.add_conditional_probability(0.3, 0.8)
marginal_space.get_probabilities()
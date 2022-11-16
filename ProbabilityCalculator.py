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

# P(x|y) = P(y|x_1)P(x_1) / (p(y|x_1)*p(x_1) + p(y|x_2)p(x_2))
marginal_space = MarginalSpace()
marginal_space_element1 = marginal_space.add_conditional_probability(0.7, 0.2)
marginal_space_element2 = marginal_space.add_conditional_probability(0.3, 0.8)

# P(state=clean | u, state=dirty) = 0.8 * P(state = dirty) = 0.8 * 0.6
# P(state=clean | u, state=clean) = 1.0 * P(state = clean) = 1.0 * 0.4
# P(state=dirty | u, state=dirty) = 0.2 * P(state = dirty) = 0.2 * 0.6
# P(state=dirty | u, state=clean) = 0.0 * P(state = clean) = 0.0 * 0.4
# P(state=clean | u) = P()

clean = State(0.4)
dirty = State(0.6)
# The probability of clean given previous was dirty is 0.8
clean.given_previous_was(dirty, 0.8)
clean.given_previous_was(clean, 1)
dirty.given_previous_was(dirty, 0.2)
dirty.given_previous_was(clean, 0)

clean.estimate()
dirty.estimate()
# P(s=y | t=y) = 0.7
# P(s=y | t=w) = 0.3
# P(t=y) = 0.2
# P(t=w) = 0.8

# P(t=y | s=y) = P(s=y|t=y) * P(t=y) / P(s=y|)

ms = MarginalSpace()

ms.add_conditional_probability(0.7, 0.2)
ms.add_conditional_probability(0.3, 0.8)
print(ms.get_probabilities())
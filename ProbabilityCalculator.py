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
    
# P(x|y) = P(y|x_1)P(x_1) / (p(y|x_1)*p(x_1) + p(y|x_2)p(x_2))
marginal_space = MarginalSpace()
marginal_space_element1 = marginal_space.add_conditional_probability(0.7, 0.2)
marginal_space_element2 = marginal_space.add_conditional_probability(0.3, 0.8)
print(marginal_space.get_probabilities())
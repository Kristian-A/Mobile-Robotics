from src.probability_calculator import ProbabilityUtility as PU
from src.probability_calculator import State, MarginalSpace


# PURE BAYES!
# P(X|Y) = P(Y|X)P(X) / P(Y) = Likelihood * Prior / Evidence
likelihood = 0.2
prior = 3/8
evidence = 0.5
posterior = PU.bayes(likelihood, prior, evidence)
# print(posterior)


# MARGINALIZED BAYES!
# P(X|Y) =  P(Y|X)P(X) / (P(Y|X)P(X) + P(Y|!X)P(!X))
ms = MarginalSpace()
ms.add_conditional_probability(0.3, 0.5) # P(Y|X)P(X)
ms.add_conditional_probability(0.6, 0.5) # P(Y|!X)P(!X)
print(ms.get_probabilities()[0])

# STATE!
# P(DIRTY| u, DIRTY) = 0.2
# P(DIRTY) = 0.6, P(CLEAN) = 0.4
# P(CLEAN | u) = P(CLEAN| u, DIRTY)P(DIRTY) + P(CLEAN| u, CLEAN)P(CLEAN)
clean = State(0.4)
dirty = State(0.6)
# The probabilty of clean given previous was dirty is now 0.8.
clean.given_previous_was(dirty, 0.8) # P(CLEAN| u, DIRTY) = 0.8
clean.given_previous_was(clean, 1) # P(CLEAN| u, CLEAN) = 1.0
# print(clean.estimate())
from abc import ABC, abstractmethod
import numpy as np

class Bug(ABC):
    def __init__(self, start_point, end_point, perimiters):
        self.euclidean_distance = (start_point - end_point).l2_norm()
        self.perimiters = perimiters

    def __str__(self):
        return f'lower boundary: {self.lower_boundary()}, upper boundary: {self.upper_boundary()}'

    @abstractmethod
    def upper_boundary(self):
        pass

    @abstractmethod
    def lower_boundary(self):
        pass


class Bug1(Bug):
    
    def lower_boundary(self):    
        return self.euclidean_distance

    def upper_boundary(self):
        return self.euclidean_distance + 1.5 * np.sum(self.perimiters) 

class Bug2(Bug):

    def __init__(self, start_point, end_point, perimiters, number_of_intersections):
        super().__init__(start_point, end_point, perimiters)

        self.number_of_intersections = np.array(number_of_intersections)

    def lower_boundary(self):    
        return self.euclidean_distance

    def upper_boundary(self):
        factors = self.perimiters * self.number_of_intersections
        return self.euclidean_distance + 0.5 * np.sum(factors)
    
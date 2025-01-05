from abc import ABC, abstractmethod

class FilterStrategy(ABC):
    @abstractmethod
    def removeValues(self, val):
        pass
    
class RemoveNegativeStrategy(FilterStrategy):
    def removeValues(self, val):
        return val < 0
    
class RemoveOddStrategy(FilterStrategy):
    def removeValues(self, val):
        return abs(val) % 2
    
class Values:
    def __init__(self, values):
        self.values = values
    
    def filter(self, strategy):
        res = []
        for val in self.values:
            if not strategy.removeValues(val):
                res.append(val)
        return res
    
values = Values([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])
print(values.filter(RemoveNegativeStrategy()))  # [1, 2, 3, 4, 5]
print(values.filter(RemoveOddStrategy()))    # [2, 4, -2, -4]
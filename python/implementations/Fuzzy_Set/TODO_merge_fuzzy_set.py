import enum


class SetType(enum.IntEnum):
    DENOMBRABLE = 0
    UNDENOMBRABLE = 1


class FuzzySet():
    def __init__(self, set_type: SetType = SetType.DENOMBRABLE):
        pass

    def kernel(self):
        current_kernel = FuzzySet(SetType.DENOMBRABLE)        
        for element in self:
            if element.probability == 1:
                current_kernel.add(element)
        return current_kernel

    def support(self):
        current_support = FuzzySet(SetType.DENOMBRABLE)        
        for element in self:
            if element.probability > 0:
                current_support.add(element)
        return current_support

    def caracteristic_function(self, x):
        return self[x]

    def hauteur(self):
        return max(element.probability for element in self)

    def est_normalise(self):
        return self.hauteur() == 1

    def cardinalite(self):
        return sum(element.probability for element in self)

    def include_in(self, B: FuzzySet) -> bool:
        return all(True for element in self if element in B else False)

    def strictly_include_in(self, B: FuzzySet) -> bool:
        return self.include_in(B) and
               any(True for element in B if element not in self else False)
import copy


class ProbabilityOutOfRange(Exception):
    pass

class ObjectAlreadyInFuzzySet(Exception):
    pass

class ObjectNotInFuzzySet(Exception):
    pass

def _check_probability_range(probability: float):
    if not 0 <= probability <= 1:
        raise ProbabilityOutOfRange("The probability as an incorrect value : " + str(probability))

class FuzzySet():
    def __init__(self):
        self._content = dict()

    def __eq__(self, other_set):
        if len(self) != len(other_set):
            return False
        return all(o1 == o2 for (o1, o2) in zip(self, other_set))

    def __contains__(self, o: object):
        return o in self._content

    def __len__(self):
        return len(self._content.keys())

    def __repr__(self):
        return self._content.__repr__()

    def __str__(self):
        if self.is_empty():
            return "{}"

        s = "{"
        for key, probability in self._content.items():
            s += str(probability) + "|" + str(key) + ", "
        return s[:-2] + "}"

    def __iter__(self):
        return self._content.__iter__()

    def __getitem__(self, item: object) -> float:
        return self._content[item]

    def copy(self):
        return FuzzySet(copy.deepcopy(self._content))

    def add(self, o: object, probability: float):
        _check_probability_range(probability)
        if o in self and probability != self[o]:
            raise ObjectAlreadyInFuzzySet("The FuzzySet already contains the object : " + str(o))
        self._content[o] = probability

    def remove(self, o: object):
        """ Remove 'o' from the Set if it's inside. If it's not present, do
        nothing.
        """
        try:
            del self._content[o]
        except KeyError:
            raise ObjectNotInFuzzySet("The object " + str(o) + " is not in the FuzzySet")

    def set_probability(self, o: object, probability: float):
        _check_probability_range(probability)
        if o not in self:
            raise ObjectNotInFuzzySet("The object " + str(o) + " is not in the FuzzySet")
        self._content[o] = probability

    def is_empty(self):
        return len(self._content) == 0

    def cardinal(self) -> int:
        return len(self)



def main():
    s = FuzzySet()
    print(s)
    s.add("A", 0.4)
    print(s)
    s.add("B", 0.6)
    print(s)
    #s.add("C", 1.1)
    s.add("B", 0.7)



if __name__ == '__main__':
    main()

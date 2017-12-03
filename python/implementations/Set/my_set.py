""" An implementation of the mathematical Set.
A Set must respect properties such as :
- Can't contains the same object twice.
- Can contains different kind of object.
"""
import copy
import itertools


class Set():

    def __init__(self, content: iter = ()):
        self._content = list(set(content)) # Remove doublons in iterable

    def __eq__(self, other_set: iter):
        if len(self) != len(other_set):
            return False
        return all(o1 == o2 for (o1, o2) in zip(self, other_set))

    def __str__(self):
        return "{" + self._content.__str__()[1:-1] + "}"

    def __repr__(self):
        return self._content.__repr__()

    def __contains__(self, o: object):
        return o in self._content

    def __len__(self):
        return len(self._content)

    def __iter__(self):
        return self._content.__iter__()

    def __div__(self, o: object):
        return self.division(o)

    def __and__(self, o: iter) -> iter:
        return Set.intersection(self, o)

    def __or__(self, o: iter) -> iter:
        return Set.union(self, o)

    def copy(self):
        return Set(copy.deepcopy(self._content))

    def is_empty(self):
        return len(self._content) == 0

    def add(self, o: object):
        """ Add 'o' to the Set if it's not already present. """
        if not o in self:
            self._content.append(o)

    def remove(self, o: object):
        """ Remove 'o' from the Set if it's inside. If it's not present, do
        nothing.
        """
        self._content.remove(o)

    def cardinal(self) -> int:
        return len(self)

    @staticmethod
    def intersection(set1, set2):
        return Set(copy.deepcopy(o) for o in set1 if o in set2)

    @staticmethod
    def union(set1, set2):
        return Set(copy.deepcopy(o) for o in itertools.chain(set1, set2))

    def isdisjoint(self, other_set: iter) -> bool:
        if len(self) < len(other_set):
            smallest_set, other_set = self, other_set
        else:
            smallest_set, other_set = other_set, self
        for o in smallest_set:
            if o in self:
                return False
        return True

    def is_subset(self, other_set) -> bool:
        for o in self:
            if o not in other_set:
                return False
        return True

    def is_superset(self, other_set) -> bool:
        for o in other_set:
            if o not in self:
                return False
        return True

    def division(self, other_set):
        new_set = Set(self._content)

    @staticmethod
    def smallest(set1, set2):
        return set1 if len(set1) <= len(set2) else set2

    @staticmethod
    def largest(set1, set2):
        return set1 if len(set1) >= len(set2) else set2


EMPTY_SET = Set()
Ø = Set()


if __name__ == '__main__':
    pass

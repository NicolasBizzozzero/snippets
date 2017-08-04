from my_set import *


class TestSet():
    def test___init__():
        # We can initialise a Set correctly
        assert Set([1, 2, 3])

        # We can initialise an empty Set
        assert Set([]) == Set() == {}

        # Doublons are removed
        assert Set([1, 2, 2]) == Set([1, 2])

    def test___eq__():
        # We can compare to equals Sets
        assert Set([1, 2, 3]) == Set([1, 2, 3])

        # Set with a different length are not equals
        assert Set([1, 2, 3]) != Set([1, 2])

        # Set with differents elements and same length are not equals
        assert Set([1, 2, 3]) != Set([1, 2, 4])

    def test___str__():
        # Non-empty Set are correctly represented
        assert str(Set([1, 2, 3])) == "{1, 2, 3}"

        # Empty Set are correctly represented
        assert str(Set()) == "{}"

    def test___repr__():
        pass

    def test___contains__():
        assert 1 in Set([1, 2, 3])
        assert 1 not in Set(["1", "2", "3"])

    def test___len__():
        s = Set([1, 2, 3])        
        assert len(s) == 3

        assert len(Set()) == 0

    def test___iter__():
        def iter_items(s):
            content = []
            for o in s:
                content.append(o)
            return content
        content = iter_items(Set([1, 2, 3]))
        assert content == [1, 2, 3]

        content = iter_items(Set())
        assert content == []

    def test___div__():
        assert Set([1, 2, 3]) / Set([1, 2, 3]) == Set()
        assert Set([1, 2, 3]) / Set([1, 2]) == Set([3])
        assert Set([1, 2, 3]) / Set([4, 5, 6]) == Set([1, 2, 3])

    def test___and__():
        assert Set([1, 2, 3]) & Set([1, 2, 3]) == Set([1, 2, 3])
        assert Set([1, 2, 3]) & Set([1, 2, 3, 4]) == Set([1, 2, 3])
        assert Set([1, 2, 3, 4]) & Set([1, 2, 3]) == Set([1, 2, 3])
        assert Set([1, 2, 3]) & Set([4]) == Set()
        assert Set([1, 2, 3]) & Set() == Set()
        assert Set() & Set() == Set()
        
    def test___or__():
        assert Set([1, 2, 3]) | Set([1, 2, 3]) == Set([1, 2, 3])
        assert Set([1, 2, 3]) | Set([1, 2, 3, 4]) == Set([1, 2, 3, 4])
        assert Set([1, 2, 3, 4]) | Set([1, 2, 3]) == Set([1, 2, 3, 4])
        assert Set([1, 2, 3]) | Set([4]) == Set([1, 2, 3, 4])
        assert Set([1, 2, 3]) | Set() == Set([1, 2, 3])
        assert Set() | Set() == Set()

    def test_copy():
        s = Set([1, 2, 3])
        s_copy = s.copy()
        assert s == s_copy


    def test_is_empty():
        assert Set().is_empty() == True

    def test_add():
        s = Set([1, 2, 3])
        s.add("5")
        assert "5" in s

        s.add(5)
        assert 5 in s and "5" in s

    def test_remove():
        s = Set([1, 2, 3])
        s.add("5")
        s.remove("5")
        assert "5" not in s


def call_all_method_from_class(c, predicat=(lambda s: True)):
    """ Call all the method from the class c. The optional argument predicat is
    a function who check if the name of the method which's gonna be called
    respect a custom condition. 
    """
    try:
        for method in dir(c):
            if predicat(method):
                method_to_call = getattr(c, method)
                method_to_call()
    except TypeError:
        pass


def main():
    call_all_method_from_class(TestSet, predicat=lambda s:  s[:4] == "test")

if __name__ == '__main__':
    main()

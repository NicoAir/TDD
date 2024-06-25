from kata2 import add
from pytest import raises

def testAddZero():
    assert add("") == 0

def testAddOne():
    assert add("1") == 1

def testAddTwo():
    assert add("1,2") == 3
    assert add("1\n2") == 3

def testAddThree():
    assert add("1,2,3") == 6
    assert add("1\n2\n3") == 6
    assert add("1,2\n3") == 6

def testAddNoTail():
    with raises(ValueError):
        add("1,")
        add("1\n")

def testAddCustomDelimiter():
    assert add("//;\n1;3") == 4
    assert add("//|\n1|2|3") == 6
    assert add("//sep\n2sep5") == 7

def testAddCustomException():
    with raises(ValueError) as exception:
        add("//|\n1|2,3")
        assert str(exception.value) == "'|' expected but ',' found at position 3."
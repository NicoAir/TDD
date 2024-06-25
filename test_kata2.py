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
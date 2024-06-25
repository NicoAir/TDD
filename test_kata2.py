from kata2 import add
from pytest import raises

def testAddZero():
    assert add("") == 0

def testAddOne():
    assert add("1") == 1

def testAddTwo():
    assert add("1,2") == 3

def testAddThree():
    with raises(ValueError):
        add("1,2,3")
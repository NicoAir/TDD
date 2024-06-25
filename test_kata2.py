from kata2 import add

def testAddZero():
    assert add("") == 0

def testAddOne():
    assert add("1") == 1

def testAddTwo():
    assert add("1,2") == 3

def testAddThree():
    assert add("1,2,3") == 6
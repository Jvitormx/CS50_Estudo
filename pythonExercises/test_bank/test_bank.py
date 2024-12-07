from bank import value

def test_0():
    assert value("Hello, dude!")==0

def test_20():
    assert value("hi, dude!")==20

def test_100():
    assert value("bye, dude!")==100

def test_Number():
    assert value("1234")==100

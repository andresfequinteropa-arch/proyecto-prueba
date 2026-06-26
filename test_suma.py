def suma(a, b):
    return a + b

def test_suma_positivos():
    assert suma(2, 3) == 5

def test_suma_negativos():
    assert suma(-1, -1) == -2

def test_suma_cero():
    assert suma(0, 5) == 5

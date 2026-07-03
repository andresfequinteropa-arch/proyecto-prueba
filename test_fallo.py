def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def test_multiplicacion():
    assert multiplicar(3, 4) == 15  # ❌ 3x4 = 12, no 15

def test_division():
    assert dividir(10, 2) == 6  # ❌ 10/2 = 5, no 6

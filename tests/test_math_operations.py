# test_math_operations.py

from math_operations import add_numbers

@pytest.mark.parametrize("funcion_generadora, resultado_esperado", [
    (saludo_espanol, "Hola, Mundo!"),
    (saludo_ingles, "Hello, World!"),
    (saludo_frances, "Bonjour, le Monde!"),
    (saludo_aleman, "Hallo, Welt!")
])

def test_add_numbers():
    assert add_numbers(3, 4) == 7
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
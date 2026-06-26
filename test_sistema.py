# ─── Módulo bajo prueba ───────────────────────────────────────────────────────

class Calculadora:
    def sumar(self, a, b): return a + b
    def restar(self, a, b): return a - b
    def multiplicar(self, a, b): return a * b
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b

class Validador:
    def es_email_valido(self, email):
        return "@" in email and "." in email.split("@")[-1]

    def es_contrasena_segura(self, pwd):
        return (len(pwd) >= 8 and
                any(c.isupper() for c in pwd) and
                any(c.isdigit() for c in pwd))

class ProcesadorTexto:
    def contar_palabras(self, texto):
        return len(texto.strip().split()) if texto.strip() else 0

    def invertir(self, texto):
        return texto[::-1]

    def es_palindromo(self, texto):
        limpio = texto.replace(" ", "").lower()
        return limpio == limpio[::-1]

class GestorInventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, nombre, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.productos[nombre] = self.productos.get(nombre, 0) + cantidad

    def retirar(self, nombre, cantidad):
        if nombre not in self.productos:
            raise KeyError(f"Producto '{nombre}' no existe")
        if self.productos[nombre] < cantidad:
            raise ValueError("Stock insuficiente")
        self.productos[nombre] -= cantidad

    def stock(self, nombre):
        return self.productos.get(nombre, 0)


# ─── Pruebas: Calculadora ─────────────────────────────────────────────────────

class TestCalculadora:
    def setup_method(self):
        self.calc = Calculadora()

    def test_suma_enteros(self):
        assert self.calc.sumar(5, 3) == 8

    def test_suma_negativos(self):
        assert self.calc.sumar(-4, -6) == -10

    def test_resta_resultado_negativo(self):
        assert self.calc.restar(3, 10) == -7

    def test_multiplicacion_por_cero(self):
        assert self.calc.multiplicar(99, 0) == 0

    def test_division_exacta(self):
        assert self.calc.dividir(10, 2) == 5.0

    def test_division_entre_cero_lanza_excepcion(self):
        import pytest
        with pytest.raises(ValueError, match="No se puede dividir entre cero"):
            self.calc.dividir(10, 0)


# ─── Pruebas: Validador ───────────────────────────────────────────────────────

class TestValidador:
    def setup_method(self):
        self.v = Validador()

    def test_email_valido(self):
        assert self.v.es_email_valido("usuario@ecci.edu.co") is True

    def test_email_sin_arroba(self):
        assert self.v.es_email_valido("usuarioecci.edu.co") is False

    def test_email_sin_punto(self):
        assert self.v.es_email_valido("usuario@ecciEduco") is False

    def test_contrasena_segura(self):
        assert self.v.es_contrasena_segura("Segura123") is True

    def test_contrasena_sin_mayuscula(self):
        assert self.v.es_contrasena_segura("segura123") is False

    def test_contrasena_muy_corta(self):
        assert self.v.es_contrasena_segura("Ab1") is False


# ─── Pruebas: ProcesadorTexto ─────────────────────────────────────────────────

class TestProcesadorTexto:
    def setup_method(self):
        self.p = ProcesadorTexto()

    def test_contar_palabras_normal(self):
        assert self.p.contar_palabras("hola mundo como estas") == 4

    def test_contar_palabras_vacio(self):
        assert self.p.contar_palabras("") == 0

    def test_invertir_texto(self):
        assert self.p.invertir("Python") == "nohtyP"

    def test_palindromo_verdadero(self):
        assert self.p.es_palindromo("anita lava la tina") is True

    def test_palindromo_falso(self):
        assert self.p.es_palindromo("ingenieria de sistemas") is False


# ─── Pruebas: GestorInventario ────────────────────────────────────────────────

class TestGestorInventario:
    def setup_method(self):
        self.g = GestorInventario()

    def test_agregar_producto(self):
        self.g.agregar("laptop", 10)
        assert self.g.stock("laptop") == 10

    def test_agregar_acumula_stock(self):
        self.g.agregar("laptop", 5)
        self.g.agregar("laptop", 3)
        assert self.g.stock("laptop") == 8

    def test_retirar_reduce_stock(self):
        self.g.agregar("mouse", 10)
        self.g.retirar("mouse", 4)
        assert self.g.stock("mouse") == 6

    def test_retirar_producto_inexistente(self):
        import pytest
        with pytest.raises(KeyError):
            self.g.retirar("teclado", 1)

    def test_retirar_mas_del_stock(self):
        import pytest
        self.g.agregar("monitor", 2)
        with pytest.raises(ValueError, match="Stock insuficiente"):
            self.g.retirar("monitor", 5)

    def test_cantidad_negativa_lanza_excepcion(self):
        import pytest
        with pytest.raises(ValueError):
            self.g.agregar("tablet", -1)

# %%
class NodoLSLC():
    def __init__(self, co, exp) -> None:
        self.co = co
        self.exp = exp
        self.siguiente = None

# %%


class LSLC():
    '''Clase que define la Lista Simplemente Ligada Circular
    - Metodo constructor que inicializa la lista
    - insertar: Metodo que agrega un nodo a la lista'''

    def __init__(self):
        self.primero = None

    def insertar(self, co: int, exp: int) -> None:
        nuevo_nodo = NodoLSLC(co, exp)

        if not self.primero:
            self.primero = nuevo_nodo
            nuevo_nodo.siguiente = self.primero
            return
        actual = self.primero
        while actual.siguiente != self.primero:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = self.primero

    def imprimir(self) -> None:
        if not self.primero:
            print("La lista está vacía.")
            return
        actual = self.primero
        resultado = ""
        while True:
            resultado += f"{actual.co}X^{actual.exp} _ "
            actual = actual.siguiente
            if actual == self.primero:
                break
        print(resultado)

    def sumarUnTermino(self, polinomio2):
        resultado = LSLC()
        actual1 = self.primero
        actual2 = polinomio2.primero
        resultado.insertar(actual1.co + actual2.co, actual1.exp)
        return resultado

    def sumarVariosTerminos(self, polinomio2):
        resultado = LSLC()
        actual1 = self.primero
        actual2 = polinomio2.primero
        while actual1.siguiente != self.primero:
            resultado.insertar(actual1.co + actual2.co, actual1.exp)
            actual1 = actual1.siguiente
            actual2 = actual2.siguiente
        resultado.insertar(actual1.co + actual2.co, actual1.exp)
        return resultado

    def sumarVariosTerminosDistintoTamano(self, polinomio2):
        resultado = LSLC()
        exp = max(self.primero.exp, polinomio2.primero.exp)
        while exp >= 0:
            sum_co = 0
            actual1 = self.primero
            actual2 = polinomio2.primero
            while actual1.siguiente != self.primero:
                sum_co += actual1.co if actual1.exp == exp else 0
                actual1 = actual1.siguiente
            sum_co += actual1.co if actual1.exp == exp else 0
            while actual2.siguiente != polinomio2.primero:
                sum_co += actual2.co if actual2.exp == exp else 0
                actual2 = actual2.siguiente
            sum_co += actual2.co if actual2.exp == exp else 0

            resultado.insertar(sum_co, exp)
            exp -= 1
        return resultado


# %%
p1 = LSLC()
p1.insertar(2, 4)
p1.insertar(-4, 2)
p1.insertar(5, 1)
p1.insertar(9, 0)
p1.imprimir()
p2 = LSLC()
p2.insertar(12, 3)
p2.insertar(78, 0)
p2.imprimir()
# %%
p3 = p1.sumarVariosTerminosDistintoTamano(p2)
# %%
p3.imprimir()
# %%

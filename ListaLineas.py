from Nodolinea import nodolinea

class listalineas:
    def __init__(self):
        self.primero=None

    def insertar(self,Linea):
        if self.primero is None:
            self.primero=nodolinea(Linea)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodolinea(Linea)

    def recorrer(self):
        actual=self.primero
        while actual:
            print("linea:",actual.linea.numero)
            actual.linea.componentes.recorrer()
            actual=actual.siguiente
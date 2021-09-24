from Nodoproducto import nodoproducto
class listasimulacionp:
    def __init__(self):
        self.primero=None

    def insertar(self,Producto):
        if self.primero is None:
            self.primero=nodoproducto(Producto)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoproducto(Producto)

    def recorrer(self):
        actual=self.primero
        while actual:
            print("Producto:",actual.producto)
            actual=actual.siguiente
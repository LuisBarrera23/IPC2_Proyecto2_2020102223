from Nodosimulacion import nodosimulacion
class listasimulacion:
    def __init__(self):
        self.primero=None

    def insertar(self,Simulacion):
        if self.primero is None:
            self.primero=nodosimulacion(Simulacion)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodosimulacion(Simulacion)

    def recorrer(self):
        actual=self.primero
        while actual:
            print("Simulacion:",actual.simulacion.nombre)
            actual.simulacion.listadoproduc.recorrer()
            actual=actual.siguiente

    def buscar(self,nombre):
        actual=self.primero
        while actual:
            if actual.simulacion.nombre==nombre:
                return actual.simulacion.listadoproduc
            actual=actual.siguiente
        return None
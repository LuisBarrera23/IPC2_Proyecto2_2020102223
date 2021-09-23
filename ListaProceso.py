from Nodoproceso import nodoproceso
class listaproceso:
    def __init__(self):
        self.primero=None

    def insertar(self,Proceso):
        if self.primero is None:
            self.primero=nodoproceso(Proceso)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoproceso(Proceso)

    def recorrer(self):
        actual=self.primero
        while actual:
            print("Linea:",actual.proceso.linea,"componente:",actual.proceso.componente)
            actual=actual.siguiente
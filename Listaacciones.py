from Nodoaccion import nodoaccion
class listaacciones:
    def __init__(self):
        self.primero=None

    def insertar(self,Accion):
        if self.primero is None:
            self.primero=nodoaccion(Accion)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoaccion(Accion)
from Nodotiempo import nodotiempo
class listatiempo:
    def __init__(self):
        self.primero=None

    def insertar(self,Tiempo):
        if self.primero is None:
            self.primero=nodotiempo(Tiempo)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodotiempo(Tiempo)
        
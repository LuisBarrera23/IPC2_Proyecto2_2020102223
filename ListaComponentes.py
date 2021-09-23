from Nodocomponente import nodocomponente
class listacomponentes:
    def __init__(self):
        self.primero=None

    def insertar(self,Componente):
        if self.primero is None:
            self.primero=nodocomponente(Componente)
        else:
            actual=nodocomponente(Componente,siguiente=self.primero)
            self.primero.anterior=actual
            self.primero=actual

    def recorrer(self):
        if self.primero is None:
            return
        actual=self.primero
        print("componente numero:",actual.componente.numero)
        while actual.siguiente:
            actual=actual.siguiente
            print("componente numero:",actual.componente.numero)

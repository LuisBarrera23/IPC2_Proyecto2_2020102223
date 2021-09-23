from Componente import componente
from ListaComponentes import listacomponentes
class linea:
    def __init__(self,numero,cComponentes):
        self.numero=numero
        self.cComponentes=cComponentes
        self.componentes=listacomponentes()
        for i in range(cComponentes,0,-1):
            nuevo=componente(i)
            self.componentes.insertar(nuevo)

        
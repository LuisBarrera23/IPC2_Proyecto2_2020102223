from Componente import componente
from ListaComponentes import listacomponentes
class linea:
    def __init__(self,numero,cComponentes,tiempo):
        self.numero=numero
        self.pos=0
        self.cComponentes=cComponentes
        self.tiempo=tiempo
        self.componentes=listacomponentes()
        for i in range(cComponentes,0,-1):
            nuevo=componente(i)
            self.componentes.insertar(nuevo)

        
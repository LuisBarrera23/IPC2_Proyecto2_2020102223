from Tiempo import tiempo
from ListaProceso import listaproceso
from ListaTiempo import listatiempo
from Listaacciones import listaacciones
class producto:
    def __init__(self,nombre,strproceso,proceso,lineas,cantidadlineas):
        self.nombre=nombre
        self.strproceso=strproceso
        self.proceso=proceso
        self.lineas=lineas
        self.cantidadlineas=cantidadlineas
        self.Tiempos=listatiempo()
        self.Ttotal=0

    def procesar(self):
        self.Tiempos=listatiempo()
        #print(self.strproceso)
        lineas=self.lineas                                      #listado de lineas
        clineas=int(self.cantidadlineas)                        #cantidad de lineas de produccion
        
        
        lineaActual=lineas.primero
        procesoactual=self.proceso.primero
        segundo=0
        while procesoactual is not None:
            ensamblado=False
            lineaActual=lineas.primero
            lineab=procesoactual.proceso.linea
            componenteb=procesoactual.proceso.componente
            #print("ensamblando:",lineab,componenteb)

            
            while lineaActual is not None:
                #print(lineaActual.linea.numero)
                if lineaActual.linea.numero==lineab:
                    while ensamblado is False:
                        #print(lineaActual.linea.pos)
                        if lineaActual.linea.pos<componenteb:
                            lineaActual.linea.pos+=1
                            segundo+=1
                            #print("iteracion segundo",segundo)
                            acciones=listaacciones()
                            for i in range(clineas):
                                if i+1==lineab:
                                    #print("linea",i+1,"moverse a C"+str(lineaActual.linea.pos))
                                    #acciones.insertar("linea "+str(i+1)+" moverse a C"+str(lineaActual.linea.pos))
                                    acciones.insertar("Moverse a C"+str(lineaActual.linea.pos))
                                else:
                                    #print("linea "+str(i+1)+" No hacer nada")
                                    #acciones.insertar("linea "+str(i+1)+" No hacer nada")
                                    acciones.insertar("No hacer nada")
                            nuevotiempo=tiempo(segundo,acciones)
                            self.Tiempos.insertar(nuevotiempo)
                        
                        if lineaActual.linea.pos>componenteb:
                            lineaActual.linea.pos-=1
                            segundo+=1
                            #print("iteracion segundo",segundo)
                            acciones=listaacciones()
                            for i in range(clineas):
                                if i+1==lineab:
                                    #print("linea",i+1,"moverse a C"+str(lineaActual.linea.pos))
                                    #acciones.insertar("linea "+str(i+1)+" moverse a C"+str(lineaActual.linea.pos))
                                    acciones.insertar("Moverse a C"+str(lineaActual.linea.pos))
                                else:
                                    #print("linea",i+1,"No hacer nada")
                                    #acciones.insertar("linea "+str(i+1)+" No hacer nada")
                                    acciones.insertar("No hacer nada")
                            nuevotiempo=tiempo(segundo,acciones)
                            self.Tiempos.insertar(nuevotiempo)

                        if lineaActual.linea.pos==componenteb:
                            t=lineaActual.linea.tiempo
            
                            for j in range(t):
                                segundo+=1
                                acciones=listaacciones()
                                #print("iteracion segundo",segundo)
                                for i in range(clineas):
                                    if i+1==lineab:
                                        #print("linea",i+1,"Ensamblando C"+str(lineaActual.linea.pos))
                                        #acciones.insertar("linea "+str(i+1)+" Ensamblando C"+str(lineaActual.linea.pos))
                                        acciones.insertar("Ensamblando C"+str(lineaActual.linea.pos))
                                    else:
                                        #print("linea",i+1,"No hacer nada")
                                        #acciones.insertar("linea "+str(i+1)+" No hacer nada")
                                        acciones.insertar("No hacer nada")
                                nuevotiempo=tiempo(segundo,acciones)
                                self.Tiempos.insertar(nuevotiempo)
                            ensamblado=True
                lineaActual=lineaActual.siguiente
            procesoactual=procesoactual.siguiente
        self.Ttotal=segundo
        print("producto ensamblado---------------------------------------")

    def reiniciarlineas(self):
        lineas=self.lineas 
        lineaActual=lineas.primero
        while lineaActual is not None:
            #print(lineaActual.linea.pos)
            lineaActual.linea.pos=0
            #print(lineaActual.linea.pos)
            lineaActual=lineaActual.siguiente

    def mostrarproceso(self):
        tiempos=self.Tiempos
        tiempoactual=tiempos.primero
        while tiempoactual is not None:
            print(tiempoactual.tiempo.segundo, end=" ")
            acciones=tiempoactual.tiempo.acciones
            accionactual=acciones.primero
            while accionactual is not None:
                print(accionactual.accion, end=",")
                accionactual=accionactual.siguiente
            tiempoactual=tiempoactual.siguiente
            print("")
    
    

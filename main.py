from ListaProceso import listaproceso
from tkinter import Button, Tk,ttk,Label,filedialog
from PIL import Image,ImageTk
from xml.dom import minidom
from ListaLineas import listalineas
from Linea import linea
from ListaProductos import listaproductos
from Producto import producto
from Proceso import proceso
from ListaSimulacion import listasimulacion
from Simulacion import simulacion
from lsimulacionp import listasimulacionp


#variables globales
ventana=Tk()
Lineas=listalineas()
Productos=listaproductos()
Simulaciones=listasimulacion()

#funciones complementarias
def isNumero(C):
    if ((ord(C) >= 48 and ord(C) <= 57)):
        return True
    else:
        return False

def isEspacio(C):
    if (ord(C)==32 or ord(C)==9 or ord(C)==10):
        return True
    else:
        return False

def generarVentana():
    global ventana

    ventana.configure(background="#008080")
    ancho=1200
    alto=700
    x=ventana.winfo_screenwidth()
    #calculamos la coordenada X donde se posicionara la ventana
    x=(x-ancho)/2
    y=ventana.winfo_screenheight()
    #calculamos la coordenada Y donde se posicionara la ventana
    y=(y-alto)/2
    ventana.geometry('%dx%d+%d+%d' % (ancho, alto, x, y))
    ventana.title("Ensambladora")

    config = ttk.Style()
    config.configure('TFrame', background='#008080')
    pestañas=ttk.Notebook(ventana)
    pestaña1 = ttk.Frame(pestañas,style="TFrame")
    pestaña2 = ttk.Frame(pestañas)
    pestaña3 = ttk.Frame(pestañas)

    #contenido pestaña 1 de cargar archivos
    pestañas.add(pestaña1, text="Cargar Archivo")
    b1=Button(pestaña1,command=lecturaMaquina,text="Cargar XML Configuración de Maquina",font=("Verdana",12),borderwidth=5,background="beige").place(x=300,y=500,height=40,width=350)
    b2=Button(pestaña1,command=lecturaSimulacion,text="Cargar XML Configuración",font=("Verdana",12),borderwidth=5,background="beige").place(x=300,y=550,height=40,width=350)
    img=Image.open("complementos\Brazos.jpg")
    imagen=ImageTk.PhotoImage(img)
    label=Label(pestaña1,width=836,height=400,image=imagen,anchor="center")
    label.image=imagen
    label.place(x=182,y=70)
    #contenido de pestaña 2 de Reportes
    pestañas.add(pestaña2, text="Reportes")
    #contenido de pestaña 3 de Ayuda
    pestañas.add(pestaña3, text="Ayuda")

    

    pestañas.pack(fill="both",expand="yes")

    
    
    ventana.mainloop()

def lecturaMaquina():
    global Lineas,Productos
    Lineas=listalineas()
    Productos=listaproductos()
    print("configuracion de la maquina")
    ruta=filedialog.askopenfile(
        title="Por favor seleccine un archivo",
        initialdir="./",
        filetypes=(
            ("Archivo XML","*.xml"),("Todos los archivos","*.*")
        )
    )
    cadena=ruta.read().lower()
    ruta.close()
    documento=minidom.parseString(cadena)

    cantidadLineas=documento.getElementsByTagName("cantidadlineasproduccion")[0].firstChild.data
    print("cantidad de lineas de produccion:",cantidadLineas)
    lLineas=documento.getElementsByTagName("lineaproduccion")
    for l in lLineas:
        numero=int(l.getElementsByTagName("numero")[0].firstChild.data)
        cantidadC=int(l.getElementsByTagName("cantidadcomponentes")[0].firstChild.data)
        tiempoE=int(l.getElementsByTagName("tiempoensamblaje")[0].firstChild.data)
        nuevalinea=linea(numero,cantidadC)
        Lineas.insertar(nuevalinea)
        #print("Linea:",numero,"con:",cantidadC,"componentes y tarda en ensamblar:",tiempoE,"segundos")
    #Lineas.recorrer()
    #actual=Lineas.primero.linea.numero
    #print(actual)

    lProductos=documento.getElementsByTagName("producto")
    for p in lProductos:
        nombre=str(p.getElementsByTagName("nombre")[0].firstChild.data)
        elaboracion=str(p.getElementsByTagName("elaboracion")[0].firstChild.data)
        
        #automata para la lectura de la elaboración
        estado=0
        numero=""
        progre=listaproceso()
        for c in elaboracion:
            if isEspacio(c):
                continue
            if estado==0:
                if c=="l":
                    estado=1
            elif estado==1:
                if isNumero(c):
                    numero+=c
                    estado=1
                if c=="p":
                    #print("linea:",int(numero),end=" ")
                    l=int(numero)
                    estado=2
                    numero=""
            elif estado==2:
                if c=="c":
                    estado=3
            elif estado==3:
                if isNumero(c):
                    numero+=c
                    estado=3
                if c=="p":
                    c=int(numero)
                    #print("componente",int(numero))
                    nuevoproceso=proceso(l,c)
                    progre.insertar(nuevoproceso)
                    estado=0
                    numero=""
        nuevoproducto=producto(nombre,elaboracion,progre)
        Productos.insertar(nuevoproducto)
        #print("producto:",nombre,"se elabora asi:",elaboracion)
    #Productos.recorrer()




def lecturaSimulacion():
    global Simulaciones
    print("estructurando simulación")
    ruta=filedialog.askopenfile(
        title="Por favor seleccine un archivo",
        initialdir="./",
        filetypes=(
            ("Archivo XML","*.xml"),("Todos los archivos","*.*")
        )
    )
    cadena=ruta.read().lower()
    ruta.close()
    documento=minidom.parseString(cadena)

    nombre=documento.getElementsByTagName("nombre")[0].firstChild.data
    #print(nombre)
    lProductos=documento.getElementsByTagName("producto")
    listap=listasimulacionp()
    for p in lProductos:
        nombre_p=p.firstChild.data
        listap.insertar(nombre_p)
        #print(nombre_p)
    nuevasimulacion=simulacion(nombre,listap)
    Simulaciones.insertar(nuevasimulacion)
    #Simulaciones.recorrer()

if __name__=='__main__':
    generarVentana()
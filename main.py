from ListaProceso import listaproceso
from tkinter import Button, Tk,ttk,Label,filedialog,messagebox
from PIL import Image,ImageTk
from xml.dom import minidom
from copy import copy
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
cantidadL=0

#elementos de interfaz globales
comboRsimulacion=ttk.Combobox()
comboSsimulacion=ttk.Combobox()

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
    pestaña2 = ttk.Frame(pestañas,style="TFrame")
    pestaña3 = ttk.Frame(pestañas,style="TFrame")
    pestaña4 = ttk.Frame(pestañas,style="TFrame")

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
    global comboRsimulacion
    pestañas.add(pestaña2, text="Reportes")
    Label(pestaña2,bg="#008080",fg="white",relief="flat" ,text="Reportes masivos", font=("arial italic", 30) ).pack()
    img2=Image.open("complementos\Reportes.png")
    imagen2=ImageTk.PhotoImage(img2)
    label=Label(pestaña2,bg="#008080",width=512,height=512,image=imagen2,anchor="center")
    label.image=imagen2
    label.place(x=50,y=100)
    Label(pestaña2,bg="#008080",fg="white",relief="flat" ,text="Simulación", font=("arial italic", 30) ).place(x=600,y=250)
    
    comboRsimulacion=ttk.Combobox(pestaña2,state="readonly",font=("arial italic", 18))
    comboRsimulacion.place(x=600,y=350)
    comboRsimulacion.configure(width=27)

    b3=Button(pestaña2,command=masivoHTML, text="Reporte Masivo HTML",font=("Verdana",12),borderwidth=5,background="beige").place(x=600,y=420,height=40,width=350)
    b4=Button(pestaña2,command=masivoXML,text="Reporte Masivo XML",font=("Verdana",12),borderwidth=5,background="beige").place(x=600,y=470,height=40,width=350)

    #contenido de pestaña 3 de Simulación
    global comboSsimulacion
    pestañas.add(pestaña3, text="Simulación por producto")
    Label(pestaña3,bg="#008080",fg="white",relief="flat" ,text="Simulacion individual", font=("arial italic", 30) ).pack()
    Label(pestaña3,bg="#008080",fg="white",relief="flat" ,text="Nombre de la Simulación", font=("arial italic", 18) ).place(x=20,y=120)
    comboSsimulacion=ttk.Combobox(pestaña3,state="readonly",font=("arial italic", 18))
    comboSsimulacion.place(x=20,y=150)
    comboSsimulacion.configure(width=23)
    comboSsimulacion.bind('<<ComboboxSelected>>', sIndividual)




    #contenido de pestaña 4 de Ayuda
    pestañas.add(pestaña4, text="Ayuda")

    

    pestañas.pack(fill="both",expand="yes")

    
    ventana.mainloop()

def lecturaMaquina():
    global Lineas,Productos,cantidadL
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
    cantidadL=int(cantidadLineas)
    print("cantidad de lineas de produccion:",cantidadLineas)
    lLineas=documento.getElementsByTagName("lineaproduccion")
    for l in lLineas:
        numero=int(l.getElementsByTagName("numero")[0].firstChild.data)
        cantidadC=int(l.getElementsByTagName("cantidadcomponentes")[0].firstChild.data)
        tiempoE=int(l.getElementsByTagName("tiempoensamblaje")[0].firstChild.data)
        nuevalinea=linea(numero,cantidadC,tiempoE)
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
        
        nuevoproducto=producto(nombre,elaboracion,progre,Lineas,cantidadLineas)
        nuevoproducto.reiniciarlineas()
        nuevoproducto.procesar()
        nuevoproducto.mostrarproceso()
        Productos.insertar(nuevoproducto)
        #print("producto:",nombre,"se elabora asi:",elaboracion)
    #Productos.recorrer()



#pestaña de reportes------------------------------------------------------------
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
    comboreportes()

def comboreportes():
    global comboRsimulacion,comboSsimulacion,Simulaciones
    comboRsimulacion["values"]=[]
    comboSsimulacion["values"]=[]
    
    simulacionactual=Simulaciones.primero
    while simulacionactual is not None:
        values = list(comboRsimulacion["values"])
        values2 = list(comboSsimulacion["values"])
        comboRsimulacion["values"] = values + [simulacionactual.simulacion.nombre]
        comboSsimulacion["values"] = values + [simulacionactual.simulacion.nombre]
        simulacionactual=simulacionactual.siguiente
    comboRsimulacion.set("Seleccione una Simulacion")
    comboSsimulacion.set("Seleccione una Simulacion")

def masivoHTML():
    global comboRsimulacion,Simulaciones,Productos,cantidadL
    simulacionseleccionada=comboRsimulacion.get()
    if simulacionseleccionada=="" or simulacionseleccionada=="Seleccione una Simulacion":
        if simulacionseleccionada=="":
            messagebox.showerror(message="No se ha introducido archivo de simulacion",title="Error")
            return
        if simulacionseleccionada=="Seleccione una Simulacion":
            messagebox.showerror(message="No ha seleccionado ninguna simulacion",title="Error")
            return
    else:
        print(simulacionseleccionada)
        productos=Simulaciones.buscar(simulacionseleccionada)
        

        f=open("Reporte.html","w",encoding='UTF-8')
        inicio="""
        <!doctype html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

        <title>Reporte Proyecto 1</title>
        </head>
        <style>
        .titulo{
            text-align: center;
            background-color: aqua;
            padding: 8px;
        }
        .cuerpo{
            background-color: white;
        }
        .contenido{
            color: white;
        }
        .inscritos{
            color:white;
            background-color: teal;
            padding: 8px;
        }
        .tabla{
            width:80%; 
            text-align: center; 
            margin-right: auto; 
            margin-left: auto;
            padding: 15px;
        }
        h1,h2{
            text-align:center;
            padding:8px;
        }
        </style>
        <body class="cuerpo">
        <div class="titulo">"""
        inicio+=f"<h1>{simulacionseleccionada}</h1></div>"

        actualproducto=productos.primero
        while actualproducto is not None:
            produc=Productos.buscar(actualproducto.producto)
            inicio+=f"<div><h2>Producto: {produc.nombre}</h2>"

            inicio+="<div class=\"tabla\"><table class=\"table table-dark table-hover\">"
            inicio+="""<thead><tr>
            <th scope="col">Tiempo(s)</th>"""
            for i in range(cantidadL):
                inicio+=f"<th scope=\"col\">Linea {i+1}</th>"
            inicio+="</tr></thead><tbody>"
            procedimiento=produc.Tiempos

            tiempoactual=procedimiento.primero
            while tiempoactual is not None:
                inicio+="<tr>"
                inicio+="<th scope=\"row\">"+str(tiempoactual.tiempo.segundo)+"</th>"
                acciones=tiempoactual.tiempo.acciones
                accionactual=acciones.primero
                while accionactual is not None:
                    inicio+="<td>"+accionactual.accion+"</td>"
                    accionactual=accionactual.siguiente
                inicio+="</tr>"
                tiempoactual=tiempoactual.siguiente

            inicio+="</tbody></table></div></div>"
            actualproducto=actualproducto.siguiente
        
                
        # for i in range(len(Tokens)):
        #     inicio+="<tr>"
        #     inicio+="<th scope=\"row\">"+str(i+1)+"</th>"
        #     inicio+="<td>"+Tokens[i].token+"</td>"
        #     inicio+="<td>"+Tokens[i].lexema+"</td>"
        #     inicio+="<td>"+str(Tokens[i].fila)+"</td>"
        #     inicio+="<td>"+str(Tokens[i].columna)+"</td>"
        #     inicio+="</tr>"
                
        #inicio+="</tbody></table></div></div>"
        
        fin="""
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
        </body>
        </html>"""
        f.write(inicio+fin)
        f.close()
        #startfile("Reporte.html")

def masivoXML():
    global comboRsimulacion,Simulaciones,Productos,cantidadL
    simulacionseleccionada=comboRsimulacion.get()
    if simulacionseleccionada=="" or simulacionseleccionada=="Seleccione una Simulacion":
        if simulacionseleccionada=="":
            messagebox.showerror(message="No se ha introducido archivo de simulacion",title="Error")
            return
        if simulacionseleccionada=="Seleccione una Simulacion":
            messagebox.showerror(message="No ha seleccionado ninguna simulacion",title="Error")
            return
    else:
        print(simulacionseleccionada)
        productos=Simulaciones.buscar(simulacionseleccionada)
        

        f=open("Reporte.xml","w",encoding='UTF-8')
        cadena=""
        cadena+="<SalidaSimulacion>"
        cadena+=f"\n\t<Nombre>\n\t\t{simulacionseleccionada}\n\t<Nombre>"
        cadena+="\n\t<ListadoProductos>"

        actualproducto=productos.primero
        while actualproducto is not None:
            cadena+="\n\t\t<Producto>"
            produc=Productos.buscar(actualproducto.producto)
            cadena+="\n\t\t\t<Nombre>"
            cadena+="\n\t\t\t\t"+produc.nombre
            cadena+="\n\t\t\t</Nombre>"
            cadena+=f"\n\t\t\t<TiempoTotal>{str(produc.Ttotal)}</TiempoTotal>"
            cadena+="\n\t\t\t<ElaboracionOptima>"
            
            procedimiento=produc.Tiempos
            tiempoactual=procedimiento.primero
            while tiempoactual is not None:
                cadena+=f"\n\t\t\t\t<Tiempo NoSegundo=\"{tiempoactual.tiempo.segundo}\">"
                acciones=tiempoactual.tiempo.acciones
                accionactual=acciones.primero
                contador=0
                while accionactual is not None:
                    contador+=1
                    cadena+=f"\n\t\t\t\t\t<LineaEnsamblaje NoLinea=\"{contador}\">"
                    cadena+="\n\t\t\t\t\t\t"+accionactual.accion
                    cadena+="\n\t\t\t\t\t</LineaEnsamblaje>"
                    accionactual=accionactual.siguiente
                tiempoactual=tiempoactual.siguiente
                cadena+="\n\t\t\t\t</Tiempo>"

            cadena+="\n\t\t\t</ElaboracionOptima>"
            cadena+="\n\t\t</Producto>"
            actualproducto=actualproducto.siguiente
        cadena+="\n\t</ListadoProductos>"
        cadena+="\n</SalidaSimulacion>"
        

        f.write(cadena)
        f.close()
        #startfile("Reporte.html")
#pestaña de simulacion----------------------------------------------------------
def sIndividual(event):
    global comboSsimulacion
    print(comboSsimulacion.get())


if __name__=='__main__':
    generarVentana()
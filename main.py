from tkinter import Button, Tk,ttk


#variables globales
ventana=Tk()

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

    
    pestañas.add(pestaña1, text="Cargar Archivo")
    pestañas.add(pestaña2, text="Reportes")
    pestañas.add(pestaña3, text="Ayuda")

    b1=Button(pestaña1,text="Cargar XML Configuración de Maquina",font=("Verdana",12),borderwidth=5,background="beige").place(x=300,y=250,height=40,width=350)
    b1=Button(pestaña1,text="Cargar XML Configuración",font=("Verdana",12),borderwidth=5,background="beige").place(x=300,y=300,height=40,width=350)

    pestañas.pack(fill="both",expand="yes")

    
    
    ventana.mainloop()


if __name__=='__main__':
    generarVentana()
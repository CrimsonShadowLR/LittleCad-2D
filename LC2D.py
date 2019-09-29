from tkinter import *

def destruirVentana(Ventana):
	Ventana.destroy()

def IntroducirLinea(Matriz,VentanAuxiliar,entr1,entr2,entr3,entr4):
	pos1=entr1.get()
	pos2=entr2.get()
	pos3=entr3.get()
	pos4=entr4.get()
	destruirVentana(VentanAuxiliar)
	coord1=int(pos1)
	coord2=int(pos2)
	coord3=int(pos3)
	coord4=int(pos4)
	punto=Label(Matriz, text='.')
	punto.grid(row=coord2, column=coord1)	
	punto=Label(Matriz, text='.')
	punto.grid(row=coord4, column=coord3)

def AgregarLinea(Matriz, var):
	VentanAuxiliar=Tk()
	etiq1=Label(VentanAuxiliar, text="Posicion inicial X")
	etiq2=Label(VentanAuxiliar, text="Posicion inicial Y")
	etiq3=Label(VentanAuxiliar, text="Posicion final X")
	etiq4=Label(VentanAuxiliar, text="Posicion final Y")
	entr1=Entry(VentanAuxiliar)
	entr2=Entry(VentanAuxiliar)
	entr3=Entry(VentanAuxiliar)
	entr4=Entry(VentanAuxiliar)
	etiq1.grid(row=0,column=0)
	etiq2.grid(row=1,column=0)
	etiq3.grid(row=2,column=0)
	etiq4.grid(row=3,column=0)
	entr1.grid(row=0,column=1)
	entr2.grid(row=1,column=1)
	entr3.grid(row=2,column=1)
	entr4.grid(row=3,column=1)
	B=Button(VentanAuxiliar, text="OK",command=lambda:IntroducirLinea(Matriz,VentanAuxiliar,entr1,entr2,entr3,entr4))
	B.grid(row=4, column=1)

def AgregarCirculo(Matriz, var):
	VentanAuxiliar=Tk()
	etiq1=Label(VentanAuxiliar, text="Centro")
	etiq2=Label(VentanAuxiliar, text="Radio X")
	etiq3=Label(VentanAuxiliar, text="Radio Y")
	entr1=Entry(VentanAuxiliar)
	entr2=Entry(VentanAuxiliar)
	entr3=Entry(VentanAuxiliar)
	etiq1.grid(row=0,column=0)
	etiq2.grid(row=1,column=0)
	etiq3.grid(row=2,column=0)
	entr1.grid(row=0,column=1)
	entr2.grid(row=1,column=1)
	entr3.grid(row=2,column=1)

def AgregarRectangulo(Matriz, var):
	VentanAuxiliar=Tk()
	etiq1=Label(VentanAuxiliar, text="Posicion esquina superior izquierda")
	etiq2=Label(VentanAuxiliar, text="Posicion esquina inferior derecha")
	entr1=Entry(VentanAuxiliar)
	entr2=Entry(VentanAuxiliar)
	etiq1.grid(row=0,column=0)
	etiq2.grid(row=1,column=0)
	entr1.grid(row=0,column=1)
	entr2.grid(row=1,column=1)

def AgregarTriangulo(Matriz, var):
	pass

def MostrarDibujo(Matriz):
	Matriz.destroy()
	Matriz=Tk()
	Matriz.resizable(0,0)
	Matriz.geometry("630x350")

def LeerDibujo(Matriz, var):
	pass

def GrabarDibujo(Matriz, var):
	pass

def Cerrar(Menu,Matriz):
	Menu.destroy()
	Matriz.destroy()

def ObtenerVar(Menu, entrada, Matriz, var):
	var=entrada.get()
	entrada.delete(0,'end')
	if var=='1': AgregarLinea(Matriz, var)
	elif var=='2': AgregarCirculo(Matriz, var)
	elif var=='3': AgregarRectangulo(Matriz, var)
	elif var=='4': AgregarTriangulo(Matriz, var)
	elif var=='5': MostrarDibujo(Matriz)
	elif var=='6': LeerDibujo(Matriz, var)
	elif var=='7': GrabarDibujo(Matriz, var)
	elif var=='0': Cerrar(Menu,Matriz)



	

raiz=Tk()

NVentana=Tk()
NVentana.resizable(0,0)
NVentana.geometry("630x350")

raiz.resizable(0,0)

Titulo=Label(raiz, text="Menú")

Titulo.grid(row=0, column=0)

op1=Label(raiz, text="1. Agregar una linea")

op1.grid(row=1, column=0, sticky="w")

op2=Label(raiz, text="2. Agregar una elipse o circulo")

op2.grid(row=2, column=0, sticky="w")

op3=Label(raiz, text="3. Agregar un rectangulo o cuadrado")

op3.grid(row=3, column=0, sticky="w")

op4=Label(raiz, text="4. Agregar un triangulo")

op4.grid(row=4, column=0, sticky="w")

op5=Label(raiz, text="5. Mostrar un dibujo")

op5.grid(row=5, column=0, sticky="w")

op6=Label(raiz, text="6. Leer un dibujo")

op6.grid(row=6, column=0, sticky="w")

op7=Label(raiz, text="7. Grabar un dibujo")

op7.grid(row=7, column=0, sticky="w")

op0=Label(raiz, text="0. Salir del programa")

op0.grid(row=9, column=0, sticky="w")

opcion=StringVar()

entrada=Entry(raiz, text=opcion)

entrada.grid(row=8, column=0)

entrada.config(justify="center")

B=Button(raiz, text="OK",command=lambda:ObtenerVar(raiz, entrada,NVentana,opcion))

B.grid(row=8, column=1)



raiz.mainloop()

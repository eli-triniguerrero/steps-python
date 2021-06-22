#TKINTER interfaz por defecto de Python
#https://docs.python.org/es/3/library/tkinter.html
from tkinter import *
# construir mensajes emergentes
from tkinter import messagebox
#database
import sqlite3


root=Tk()
#definiendo variable para el navbar desde la raiz
navbarMenu = Menu(root)
#definiendo tamaño del navbar
root.config(menu=navbarMenu, width=300, height=300)

#BASE DE DATOS
bdMenu = Menu(navbarMenu, tearoff=0)
#haciendo submenu del menu
bdMenu.add_command(label="Conectar")
bdMenu.add_command(label="Salir")

#OPCION BORRAR
deleteMenu = Menu(navbarMenu, tearoff=0)
deleteMenu.add_command(label="Borrar")

#OPCION CRUD
crudMenu = Menu(navbarMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

#OPCION AYUDA
helpMenu = Menu(navbarMenu, tearoff=0)
helpMenu.add_command(label="Instrucciones")
helpMenu.add_command(label="Acerca de ...")

#especificando que los elementos construidos arriba se agreguen al navbar con la etiqutea bdMenu
navbarMenu.add_cascade(label="BBDD", menu=bdMenu)
navbarMenu.add_cascade(label="Borrar", menu=deleteMenu)
navbarMenu.add_cascade(label="CRUD", menu=crudMenu)
navbarMenu.add_cascade(label="Ayuda", menu=helpMenu)

root.mainloop()


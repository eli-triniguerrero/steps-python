#TKINTER interfaz por defecto de Python
#https://docs.python.org/es/3/library/tkinter.html
from tkinter import *
# construir mensajes emergentes
from tkinter import messagebox
#database
import sqlite3
#importando modulo
#from form import *

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

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
#Definiendo Frame inputs
myFrame = Frame(root)
#empaquetado
myFrame.pack()

#entry
inputID = Entry(myFrame)
#definiendo posicion
inputID.grid(row=0,column=1,padx=10, pady=10)

inputName = Entry(myFrame)
inputName.grid(row=1,column=1,padx=10, pady=10)
inputName.config(fg="red", justify="right")

inputLastName = Entry(myFrame)
inputLastName.grid(row=2,column=1,padx=10, pady=10)
inputLastName.config(fg="red", justify="right")

inputPass = Entry(myFrame)
inputPass.grid(row=3,column=1,padx=10, pady=10)
inputPass.config(show="X")

inputAddress = Entry(myFrame)
inputAddress.grid(row=4,column=1,padx=10, pady=10)

textareaComments = Text(myFrame)
textareaComments.grid(row=5,column=1,padx=10, pady=10)

#barra desplazamiento
scrollVert = Scrollbar(myFrame, command=textareaComments.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textareaComments.config(yscrollcommand=scrollVert.set)

#definiendo labels
labelID = Label(myFrame, text="ID:")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)

labelName = Label(myFrame, text="Name:")
labelName.grid(row=1, column=0, sticky="e", padx=10, pady=10)

labelLastName = Label(myFrame, text="Last Name:")
labelLastName.grid(row=2, column=0, sticky="e", padx=10, pady=10)

labelPass = Label(myFrame, text="Password:")
labelPass.grid(row=3, column=0, sticky="e", padx=10, pady=10)

labelAddress = Label(myFrame, text="Address:")
labelAddress.grid(row=4, column=0, sticky="e", padx=10, pady=10)

labelComments = Label(myFrame, text="Comments:")
labelComments.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#-.-.-.-.-.buttons
footerFrame = Frame(root)
footerFrame.pack()

btnCreate = Button(footerFrame, text="Create")
btnCreate.grid(row=1, column=0, sticky="e", padx=10, pady=10)

btnRead = Button(footerFrame, text="Read")
btnRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)

btnUpdate = Button(footerFrame, text="Update")
btnUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

btnDelete = Button(footerFrame, text="Delete")
btnDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()





from tkinter import *

root=Tk()
#defiendo campos input
#frame que esta dentro del root
myFrame = Frame()
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
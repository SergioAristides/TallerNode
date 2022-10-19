

from tkinter import Menu
from listaSimple import Linkedlist
from menuPrincipal import Menu
from listaDoble import listDoble


if __name__== '__main__':
    mylist=Linkedlist()
    list_doble=listDoble()
    menu= Menu(mylist,list_doble)
    menu.lista_a_trabajar()
    
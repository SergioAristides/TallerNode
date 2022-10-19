from inspect import Attribute
from listaSimple import Node
from listaSimple import Linkedlist
import math
from colorama import *
init()



class Menu:
    def __init__(self,linkedlist,linkedlist_doble):
        self.linkedlist=linkedlist
        self.linkedlist_doble= linkedlist_doble
        
    
    #Menu principal
    def menu(self):
        print("---lista simple---")
        print(self.linkedlist)
        print("---lista doble---")
        print(self.linkedlist_doble)
        bandera=True
        while bandera:
            
                opcion=str(input(Fore.BLUE+"\ta --->Listas simplemente enlazada\n \tb--->Listas doblemente enlazadas\n   \tc---> Salir (cancela la ejecución del programa)\n"))
                
                if(opcion == 'a'or opcion=='b' or opcion=="c"):
                    bandera=False
                    return opcion
                else:
                    print("dato invalido")
                    
    ##funcion inicializadora         
    def lista_a_trabajar(self):
        opcion=self.menu()
        print(opcion)
        if(opcion=='a'):
            self.sub_menu_simple()
        elif(opcion=='b'):
            self.sub_menu_doble()
        else:
            print("termino la ejecucion")
    #subMenu escoger Simple
    def sub_menu_escoger(self):
        bandera=True
        while bandera:
            
                option=str(input(Fore.GREEN+"\ta. Añadir nodo\n\t\t 1-> Al inicio \n\t\t2-> Al final \n\t\t3 -> En una posición específica \n \tb. Eliminar nodo\n\t\t1. Al inicio\n\t\t2. Al final\n\t\t3. En una posición específica\n\tc. Consultar valor contenido en el nodo\n\td. Modificar valor de nodo\n\te. Invertir toda la lista\n\tf. Validación especial\n"))
                if(option == 'a'or option=='b' or option=="c"or option=="d"or option=="e"or option=="f"):
                    bandera=False
                    return option
                else:
                    print("dato invalido")
            
        
    #sub menu lista simple que valida que ruta cogio el usuario
    def sub_menu_simple(self):
        option=self.sub_menu_escoger()
        if option=='a'or option =='b':
            while True:
                try:
                    num_option=int(input("ingrese el numeral: "))
                    if(num_option ==1 or num_option==2 or num_option==3):
                        break
                    else:
                        print("--ingrese un numeral valido-- ")
                except:
                    print("--dato invalido--")
            if option=='a':
                self.add_lista_simple(num_option)
                self.lista_a_trabajar()
            elif option=='b':
                self.delete_nodo_simple(num_option)
                self.lista_a_trabajar()
            
                
        else:
            if option =='c':
                while True:
                    try:
                        index= int(input("ingrese el indice a consultar: "))
                        value=self.linkedlist.consultar_valor_node(index)
                        print("el valor es: " +str(value))
                        break
                        
                    except:
                        print("---ingrese un indice valido---")
        
                self.lista_a_trabajar()
            elif option=='d':
                self.modificar_lista_simple()
                self.lista_a_trabajar()
            elif option=='e':
                self.linkedlist.reverse()
                print(self.linkedlist)
                self.lista_a_trabajar()
            elif option=='f':
                self.validacion_especial_simple()
                self.lista_a_trabajar()
    
    #agrega de diferentes formas los nodos introducidos
    def add_lista_simple(self,num_option):
        bandera=True
        if num_option ==1:
            nodo=input("ingrese el nodo: ")
            self.linkedlist.append_first(nodo)
        elif num_option==2:
            nodo=input("ingrese el nodo: ")
            self.linkedlist.push_node(nodo)
        elif num_option==3:
            while bandera:
                try:
                    index=int(input("ingrese el indice a insertar: "))
                    print(self.linkedlist.size)
                    nodo=input(Fore.RED+"ingrese el nodo: ")
                    self.linkedlist.insert_node(index,nodo)
                    bandera=False
                except :
                    print("---ingrese un indice por favor--")
    #elimina de diferentes formas los nodos introducidos
    def delete_nodo_simple(self,num_option):
        bandera=True
        if num_option ==1:
            self.linkedlist.remove_begin()
        elif num_option==2:
            self.linkedlist.remove_end()
        elif num_option==3:
            while bandera:
                try:
                    index=int(input("ingrese el indice"))
                    self.linkedlist.remove_position(index)
                    bandera=False
                except AttributeError:
                    print(AttributeError)
    #Realiza el punto d de la lista simple
    def modificar_lista_simple(self):
        while True:
            try:
                delete=int((input("ingrese el indice del nodo a modificar: ")))
                modificar=(input("ingrese el valor del nodo nuevo: "))
                self.linkedlist.modificar_node(delete,modificar)
                break
            except:
                print("indice invalido")
    def validacion_especial_simple(self):
        self.linkedlist.punto_6()
    
    #------------------------------Lista doble-------------------------------------------------------------
    #agrega de diferentes formas los nodos introducidos de la lista doble
    def validacion_especial_doble():
        pass
    def add_lista_doble(self,num_option):
        bandera=True
        if num_option ==1:
            nodo=input("ingrese el nodo: ")
            self.linkedlist_doble.append_first(nodo)
        elif num_option==2:
            nodo=input("ingrese el nodo: ")
            self.linkedlist_doble.append(nodo)
        elif num_option==3:
            while bandera:
                try:
                    index=int(input("ingrese el indice a insertar: "))
                    nodo=input(Fore.RED+"ingrese el nodo: ")
                    self.linkedlist_doble.insert_node(index,nodo)
                    bandera=False
                except :
                    print("---ingrese un indice por favor--")
    #elimina de diferentes formas los nodos introducidos de la lista doble
    def delete_nodo_doble(self,num_option):
        bandera=True
        if num_option ==1:
            self.linkedlist_doble.remove_begin()
        elif num_option==2:
            self.linkedlist_doble.remove_end()
        elif num_option==3:
            while bandera:
                try:
                    index=int(input("ingrese el indice"))
                    self.linkedlist_doble.remove_position(index)
                    bandera=False
                except AttributeError:
                    print(AttributeError)
                    
    #Modifica realiza el punto d
    def modificar_lista_doble(self):
        while True:
            try:
                delete=int((input("ingrese el indice del nodo a modificar: ")))
                modificar=(input("ingrese el valor del nodo nuevo: "))
                self.linkedlist_doble.modificar_node(delete,modificar)
                break
            except:
                print("indice invalido")
    def sub_menu_escoger_doble(self):
        bandera=True
        while bandera:
            
                option=str(input(Fore.GREEN+"\ta. Añadir nodo\n\t\t 1-> Al inicio \n\t\t2-> Al final \n\t\t3 -> En una posición específica \n \tb. Eliminar nodo\n\t\t1. Al inicio\n\t\t2. Al final\n\t\t3. En una posición específica\n\tc. Consultar valor contenido en el nodo\n\td. Modificar valor de nodo\n\te. Invertir toda la lista\n\tf. Validación especial\n\t\t1 (punto 5)\n\t\t2 (punto 6)\n"))
                if(option == 'a'or option=='b' or option=="c"or option=="d"or option=="e"or option=="f"):
                    bandera=False
                    return option
                else:
                    print("dato invalido")
    
    def sub_menu_doble(self):
        option=self.sub_menu_escoger_doble()
        if option=='a'or option =='b':
            while True:
                try:
                    num_option=int(input("ingrese el numeral: "))
                    if(num_option ==1 or num_option==2 or num_option==3):
                        break
                    else:
                        print("--ingrese un numeral valido-- ")
                except:
                    print("--dato invalido--")
            if option=='a':
                self.add_lista_doble(num_option)
                self.lista_a_trabajar()
            elif option=='b':
                self.delete_nodo_doble(num_option)
                self.lista_a_trabajar()
            elif option=='f':
                self.validacion_especial_doble()
                self.lista_a_trabajar()
            
                
        else:
            if option =='c':
                while True:
                    try:
                        index= int(input("ingrese el indice a consultar: "))
                        value=self.linkedlist_doble.consultar_valor_node(index)
                        print("el valor es: " +str(value))
                        break
                        
                    except:
                        print("---ingrese un indice valido---")
        
                self.lista_a_trabajar()
            elif option=='d':
                self.modificar_lista_doble()
                self.lista_a_trabajar()
            elif option=='e':
                self.linkedlist_doble.reverse()
                self.lista_a_trabajar()
            
                

        
        

        
    
        
        
        
    
        
    
                
                    
                

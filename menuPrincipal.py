from ossaudiodev import SOUND_MIXER_TREBLE
from listaSimple import Linkedlist


class menu:
    def __init__(self,list):
        self.list=list
        
    def menu():
        bandera=True
        while bandera:
            try:
                opcion=str(input("\ta --->Listas simplemente enlazada\n b--->Listas doblemente enlazadas\n c---> Salir (cancela la ejecución del programa)"))
                bandera = False
            except:
                print("ingrese un valor valido")
        if opcion=='a'or opcion=='b':
            return opcion
        else:
            return 0
    
    
    def lista_a_trabajar():
        opcion=menu()
        if opcion!=0:
            if(opcion=='a'):
                self.sub_menu_simple()
            elif(opcion=='b'):
                sub_menu_doble()
        else:
            print("termino la ejecucion")
        
    def sub_menu_simple():
        list=Linkedlist()
        option=str(input("\ta. Añadir nodo\n 1-> Al inicio \n 2-> Al final \n3 -> En una posición específica \n b. Eliminar nodo\n1. Al inicio\n2. Al final\n3. En una posición específica\nc. Consultar valor contenido en el nodo\nd. Modificar valor de nodo\ne. Invertir toda la lista\nf. Validación especial\n1-> Punto 5\n2->. Punto 6"))
        if option=='a'or option =='b'or option=='f':
            nunOption=int(input("ingrese el numeral"))
        else:
            if option =='c':
                print(list)
            elif option=='d':
                list
            elif option=='f':
                validacion_especial()
            
    def sub_menu_doble():
        list=Linkedlist()
        option=str(input("\ta. Añadir nodo\n 1-> Al inicio \n 2-> Al final \n3 -> En una posición específica \n b. Eliminar nodo\n1. Al inicio\n2. Al final\n3. En una posición específica\nc. Consultar valor contenido en el nodo\nd. Modificar valor de nodo\ne. Invertir toda la lista\nf. Validación especial\n1-> Punto 5\n2->. Punto 6"))
        if option=='a'or option =='b'or option=='f':
            nunOption=int(input("ingrese el numeral"))
        else:
            if option =='c':
                print(list)
            elif option=='d':
                list
            elif option=='f':
                validacion_especial()
        
    def validacion_especial():
        pass
        
    
        
        
        
    
        
    
                
                    
                

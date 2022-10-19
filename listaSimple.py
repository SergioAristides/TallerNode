from logging import exception
from os import remove
import math


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
    def __str__(self):
        return str(self.value)
    
    
class Linkedlist:
    def __init__(self):
        self.first=None
        self.size=0
        self.tail=None
    
    def append_first(self, value):
        new_node = Node(value)
        if self.first == None and self.tail == None:
            self.first = new_node
            self.tail = new_node
        else:
            new_node.next = self.first
            
            self.first = new_node
        self.size += 1
    def remove_begin(self):
        if self.first is None:
            return -1
        else:
            self.first=self.first.next
        
    def remove_end(self):
        if self.first is None:
            return -1
        elif self.first.next is None:
            self.first=None
        else:
            current=self.first
            while current.next.next !=None:
                current=current.next
            current.next=None
        
        
    def remove_value(self,value):
        if self.size==0:
            return False
        else:
            current=self.first
            try:
                while current.next.value != value:
                    current=current.next
                deleted_node=current.next
                current.next=deleted_node.next
            except AttributeError:
                print(AttributeError)
                return False
        self.size-=1
        return deleted_node
        
        
    def __len__(self):
        return self.size
        
    def __str__(self):
        String= "["
        current=self.first
        while current !=None:
            String+=str(current)
            if(current.next!=None):
                String+=str(",")
            current=current.next
        String+="]"
        return String
    
    def remove_position(self, position):
        if position != 1:
            current = self.first
            i = 1
            while current.next != None and i < position - 1:
                current = current.next
                i += 1
            if current.next != None:
                current.next = current.next.next
                return True
            else:
                return False
        else:
            self.first= self.first.next
            return True
        
            
    
            
    def insert_node(self, index, value):
        if index <= 0  or index > self.size+1:
            print('------!posicion erronea!--------')
        elif index == 1:
            self.append_first(value)
        elif index == self.size+1:
            self.push_node(value)
        else: 
            previous_node = self.get_node(index-1)
            new_node = Node(value)
            next_node = previous_node.next
            previous_node.next = new_node
            new_node.next = next_node
            self.size +=1
            
    def get_node(self, index):
        if index < 1 or index > self.size:
            return None
        elif index == 1:
            return self.first
        elif index == self.size:
            return self.tail
        else:
            current_node = self.first
            node_counter = 1
            while(index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node
            
    def reverse(self):
        prev=None
        current =self.first
        tmp=self.first.next
        
        while current !=None:
            tmp=current.next
            current.next =prev
            prev=current
            current=tmp
            
        self.first=prev    
        return self.first
    
    def modificar_node(self,index,value):
        index-=1
        new_node = Node(value)
        if index>=0 and index<self.size:
            current=self.first
            for i in range(index):
                current=current.next
            
            current.value=new_node
        else:
            raise("indice invalido")
        
    def consultar_valor_node(self,index):
        index-=1
        if index>=0 and index<self.size:
            current=self.first
            for i in range(index):
                current=current.next
            
            return current.value
        else:
            raise("indice invalido")
    
    def push_node(self, value):
        new_node = Node(value)
        if self.first == None and self.tail == None:
            self.first = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def punto_6(self):
        self.reverse()
        current=self.first
        if self.size==1:
            raiz=current.value
            raiz= math.sqrt(raiz)
            new_node=Node(raiz)
            current.value=new_node
        while current.next!=None:
            raiz=current.value
            current=current.next
            raiz= math.sqrt(raiz)
            new_node=Node(raiz)
            current.value=new_node
        
    def valor_node(self, index):
        if index < 1 or index > self.size:
            print('---No se encontro---')
        elif index == 1:
            print(self.first.value)
        elif index == self.size:
            print(self.tail.value)
        else:
            current_node = self.first
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            print(current_node.value)
            
    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            new_tail = current_node
            while(current_node.next != None):
                new_tail = current_node
                current_node = current_node.next
            self.tail = new_tail
            self.tail.next = None
            self.length -=1
            
    def validar_existe_nodo(self,value):
        bandera = False
        current=self.first

        if self.size ==1 and current.value==value:
            print("---no pude insertar un nodo del mismo valor---")
        else:
            while current.next !=None:
                if current.value== value:
                    print("---no puede insertar este nodo ya esta---")
                    bandera =True
                current= current.next
        return bandera
        
    
    def modificar_node(self,index,value):
        index-=1
        new_node = Node(value)
        if index>=0 and index<self.size:
            current=self.first
            for i in range(index):
                current=current.next
            
            current.value=new_node
        else:
            raise("indice invalido")
            
            
            
            
            
        
        
        
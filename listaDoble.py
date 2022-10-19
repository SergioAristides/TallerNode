

from turtle import position


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previous= None
        
    def __str__(self):
        return str(self.value)
    
class listDoble:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size=0
    
    def insert_node(self, index, value):
        if index <= 0 or index > self.size+ 1:
            print('posicion erronea')
        elif index == 1:
            self.append_first(value)
        elif index == self.size + 1:
            self.append(value)
        else:
            new_node = self= Node(value)
            previous_node = self.get_node(index - 1)
            next_node = self.get_node(index)
            new_node.next = next_node
            previous_node.next = new_node
            new_node.previous = previous_node
            next_node.previous = new_node
            self.size += 1
    def vacia(self):
        return self.primero==None
    def append(self, value):
        if self.vacia():
            self.primero=self.ultimo=new_node=Node(value)
        else:
            aux=self.ultimo
            self.ultimo=aux.next= new_node=Node(value)
            self.ultimo.previous=aux
            
        self.size +=1
        
    def append_first(self, value):
        if self.vacia():
            self.primero=self.ultimo=new_node=Node(value)
        else:
            aux= new_node=Node(value)
            aux.next=self.primero
            self.primero.previous=aux
            self.primero=aux
        self.size+=1
        
    def remove_begin(self):
        if self.vacia():
            print(-1)
        elif self.primero.next==None:
            self.primero=self.ultimo==None
            self.size=0
            
        else:
            self.primero=self.primero.next
            self.primero.previous=None
            self.size-=1
            
    def remove_end(self):
        if self.vacia():
            print(-1)
        if self.primero.next ==None:
            self.primero=self.ultimo=None
            self.size=0
        else:
            self.ultimo=self.ultimo.previous
            self.ultimo.next=None
            self.size-=1

                
                
    def reverse(self):
        if self.vacia():
            print(-1)
            return 
        p = self.primero
        q = p.next
        p.next = None
        p.previous = q
        while q is not None:
            q.previous = q.next
            q.next = p
            p = q
            q = q.previous
        self.primero = p
                
    
    
    def modificar_node(self,index,value):
        index-=1
        new_node = Node(value)
        if index>=0 and index<self.size:
            current=self.primero
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
    
    def get_node(self, index):
        if index < 1 or index > self.size:
            return None
        elif index == 1:
            return self.primero
        elif index == self.size:
            return self.ultimo
        else:
            current_node = self.primero
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node
    
    def remove_psition(self, index):
        if index == 1:
            self.ca_node()
        elif index == self.length:
            self.pop_node()
        else:
            remove_node = self.get_node(index)
            if remove_node != None:
                previous_node = self.get_node(index - 1)
                next_node = self.get_node(index + 1)
                previous_node.next = next_node
                next_node.previous = previous_node
                self.size -= 1
                
    def ca_node(self):
        if self.size == 0:
            self.primero = None
            self.ultimo = None
        elif self.primero != None:
            remove_node = self.primero
            self.primero = remove_node.next
            remove_node.next = None
            self.size -= 1
            
    def pop_node(self):
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            remove_node = self.tail
            self.tail = remove_node.previous
            self.tail.next = None
            remove_node.previous = None
            self.length -= 1
    def modificar_node(self, index, value):
        buscar = self.get_node(index)
        if buscar != None:
            buscar.value = value
        else:
            return None
    def consultar_valor_node(self,index):
        index-=1
        if index>=0 and index<self.size:
            current=self.primero
            for i in range(index):
                current=current.next
            
            return current.value
        else:
            raise("indice invalido")
        
    def __str__(self):
        aux= self.primero
        string="["
        while aux:
            string+=str(aux.value)
            if(aux.next!=None):
                string+=","
            aux=aux.next
        
            
        string+="]"    
        return string
        
            
            
        
        
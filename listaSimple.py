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
        
    def append(self,value):
        Mynode=Node(value)
        if self.size==0:
            self.first= Mynode
        else:
            current= self.first
            while current.next !=None:
                current= current.next
            current.next=Mynode
            
        self.size+=1  
        return str(Mynode)
    
    def append_first(self ,value):
        myNode=Node(value)
        if self.size==0:
            self.first=myNode
        else:
            current= self.first
            self.first=myNode
            self.first.next=current
    def remove_begin(self):
        if self.first is None:
            return -1
        else:
            self.first=self.first.next
        
    def remove_end(self):
        if self.first is None:
            return -1
        elif self.first.next is None:
            self.firsy=None
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
    
    def insert(self,index):
        while True:
            if index==self.size-1:
                return self.tail.value
            elif index==0:
                return self.first.value
            elif index <0 or index >=self.size:
                index=int(input("ingrese la posicion de otro nodo"))
            else:
                pass 
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
            
    
            
    def insert_position(self, value, index):
        new_node = Node(value)

        if index == 1:
            new_node.next = self.first
            self.first = new_node
        else:
            current = self.first
            i = 1
            while current.next != None and i < index:
                current = current.next
                i += 1
            new_node.next = current.next
            current.next = new_node
            
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
    
    def existe(self,value):
        bandera=False
        current=self.first
        while current!=None:
            current=current.next
            if(current ==value):
                bandera=True
        return bandera  
    def modificarNode(self,value):
        if existe(value):
            pass
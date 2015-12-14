import ipdb

###########################################
#
# Binary Tree
#
###########################################

class Node():
    def __init__(self,patent,left,right,value):
        self.patent = next
        self.left = None
        self.right = None
        self.value = value
  
   
class BinaryTree():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,value):
        if self.head == None: # first element
            self.head = Node(None,None,value)
            self.tail = self.head
        else:
            self.tail = Node(None,self.tail,value)
    
    def remove_from_trail(self):
        if self.head == None: # linked list is empty
            print('can not remove an element from an empty linked list')
            return
        print('removing element with value {0}'.format(self.tail.value))
        self.tail = self.tail.pre
         
    
    def print_foward(self):
        c = 0
        p = self.head
        if p == None:
            print('linked list is empty')
        
        while p != None:
            c = c + 1
            print('{0} {1}'.format(c,p.value))
            p = p.next
    
    def print_backward(self):
        c = 0
        p = self.tail
        if p == None:
            print('linked list is empty')
        while p != None:
            c = c + 1
            print('{0} {1}'.format(c,p.value))
            p = p.pre
        

# Linked List Usages Examples
        
# create a linked list
linked_list = LinkedList()

linked_list.print_foward()
linked_list.print_backward()

linked_list.remove_from_trail()

linked_list.add(1)
linked_list.add(2)
linked_list.add(2)
linked_list.remove_from_trail()
linked_list.add(3)

linked_list.print_foward()
linked_list.print_backward()
    



    
   
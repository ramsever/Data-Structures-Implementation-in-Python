##################################################
#
# How to check whether there is a loop in 
# a linked list
#
##################################################
import sys
import ipdb

class Node():
    def __init__(self,pre,next,value):
        self.pre = pre
        self.next = next
        self.value= value
        self.visit = None
    
       
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,value):
        if self.head == None:
            self.head = Node(None,None,value)
            self.tail = self.head
            return
        self.tail.next = Node(self.tail,None,value)
        self.tail = self.tail.next
        
    def remove(self):
        if self.tail.pre == None:
            print('Linked List is empty')
            self.head = None
            return
        self.tail = self.tail.pre
        self.tail.next = None
        
    def pprint(self):
        p = self.head
        while p!= None:
            print('{0}'.format(p.value))
            p = p.next
    
    
def main():

    #ipdb.set_trace()
    linked_list = LinkedList()
    
    print('----------------')
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.pprint()
    print('----------------')
    linked_list.remove()
    linked_list.pprint()
    print('----------------')
    linked_list.remove()
    linked_list.pprint()
    print('----------------')
    linked_list.remove()
    linked_list.pprint()
    print('----------------')
    linked_list.remove()
    linked_list.pprint()

    
if __name__ == '__main__':
    main()
    
    
    

    
"""Implementation of Single Linked Lists"""
class Node:   #class creates nodes for the Singular link list
    def __init__(self, data):
        self.data = data #Holds the data in the cell
        self.next = None #Holds the pointer address for next node

class LinkedList:  #class for link list itself
    def __init__(self):
        self.head = None

    def append(self, data):  #insert function
        new_node = Node(data)

        if self.head is None:  #If link list is empty
            self.head = new_node
            return 
        
        last_node = self.head   #initialise last_node as the head of the node
        while last_node.next:   #while last_node does not point to Null
            last_node = last_node.next #last node points the next node
        last_node.next = new_node #the pointer of last_node points to the new_node
    
    def print_link_list(self):   #print the link list
        curr_node = self.head
        while curr_node: #while current_node is not Null
            print(curr_node.data, end=' ')
            curr_node = curr_node.next #points the next node
        print(end='\n')

    def prepend(self, data):  #Prepending function 
        new_node = Node(data)

        new_node.next = self.head  #new_node pointer points the head of the Link_List
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
         
        if not prev_node:
            print("previous node not in the list")
            return 

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

link_list = LinkedList()
link_list.append("A")
link_list.append("B")
link_list.append("C")
link_list.append("D")

link_list.prepend("E")
link_list.insert_after_node(link_list.head.next, "F")
link_list.print_link_list()
        

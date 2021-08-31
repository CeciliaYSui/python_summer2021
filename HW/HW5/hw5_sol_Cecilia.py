# --------------------------------------------------------------------------------
# Program ------------------------- Python Camp HW #5
# Developer ----------------------- Cecilia Y. Sui
# Date last updated --------------- Aug 28, 2021
# Description --------------------- Implement a singly linked list 
# Limitations --------------------- The program does not handle when the user deletes
# all nodes in the list.
# --------------------------------------------------------------------------------


class Node: 
    def __init__(self, value = None):
        self.value = value
        self.next = None # pointer to another Node 

class LinkedList:
    # --------------------------------------------------------------------------------
    # Takes a number and sets it as the value at the head of the List
    # Time Complexity: O(1) 
    # This operation initiates the class, and it is the best possible complexity class.
    # --------------------------------------------------------------------------------
    def __init__(self, head_val):
        assert type(head_val) is int, "Parameter must be an integer for initialization!"
        self.head = Node(head_val)

    # --------------------------------------------------------------------------------
    # Returns the length of the list 
    # Time Complexity: O(n)
    # The method iterates through the singly linked list from the head node to null.
    # Due to the way singly linked list is structured in our specs, this is the best possible
    # complexity class. 
    # However, if we are allowed to create a self.length variable that are kept track 
    # of for each operation we do, then the time complexity would be improved to O(1).
    # --------------------------------------------------------------------------------
    def length(self):
        curr_node = self.head
        cnt = 0
        while curr_node: 
            cnt += 1
            curr_node = curr_node.next
        return cnt

    # --------------------------------------------------------------------------------
    # Takes a number and adds it to the end of the list
    # Time Complexity: O(n)
    # Similarly, due to the way singly linked lists are structured in our specs, this is the best
    # possible time complexity class. However, if we can keep track of a tail node, 
    # the time complexity would be improved to O(1). 
    # --------------------------------------------------------------------------------
    def addNode(self, new_value):
        assert type(new_value) is int, "Parameter must be an integer to add a node!"
        curr_node = self.head
        while curr_node.next: 
            curr_node = curr_node.next
        curr_node.next = Node(new_value)
        return
    
    # --------------------------------------------------------------------------------
    # Takes a number and adds it after the after_node (input as a Node)
    # Time Complexity: O(1)
    # This is the best possible time complexity class. 
    # --------------------------------------------------------------------------------
    def addNodeAfter(self, new_value, after_node):
        assert type(new_value) is int, "new_value must be an integer to add a node!"
        assert type(after_node) is Node, "after_node must be a Node!"
        new_node = Node(new_value)
        new_node.next = after_node.next
        after_node.next = new_node
        return
    
    # --------------------------------------------------------------------------------
    # Takes a value and adds before the before_node (input as a Node)
    # Time Complexity: O(n)
    # Similarly, due to the way singly linked lists are structured, this is the best
    # possible time complexity class. 
    # --------------------------------------------------------------------------------
    def addNodeBefore(self, new_value, before_node):
        assert type(new_value) is int, "new_value must be an integer to add a node!"
        assert type(before_node) is Node, "before_node must be a Node!"
        new_node = Node(new_value)
        # if the before node is head node
        if before_node is self.head: 
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next.value != before_node.value: 
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node
        return
    
    # --------------------------------------------------------------------------------
    # Removes a node from the list
    # Time Complexity: O(n)
    # Similarly, due to the way singly linked lists are structured in our specs, 
    # this is the best possible time complexity class, since we have to iterate 
    # through the whole list (worst case).
    # --------------------------------------------------------------------------------
    def removeNode(self, node_to_remove):
        assert type(node_to_remove) is Node, "node_to_remove must be a Node!"
        # if the node to remove is head node
        if node_to_remove is self.head:
            self.head = self.head.next
        else:
            curr_node = self.head
            while curr_node.next is not node_to_remove: 
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
        return
    
    # --------------------------------------------------------------------------------
    # Takes a value, removes all nodes with that value
    # Time Complexity: O(n)
    # This is the best possible time complexity class, since we have to iterate 
    # through the whole list to search exhaustively. 
    # --------------------------------------------------------------------------------
    def removeNodesByValue(self, value):
        assert type(value) is int, "value must be an integer to remove!"
        curr_node = self.head
        prev_node = self.head
        while curr_node:
            if curr_node.value == value: 
                # head node
                if curr_node is self.head: 
                    self.head = curr_node.next
                # not head node
                else:
                    prev_node.next = curr_node.next
            else:
                # if 2 consecutive nodes are removed, we keep the prev_node
                prev_node = curr_node
            curr_node = curr_node.next
        return
    
    # --------------------------------------------------------------------------------
    # Reverses the order of the linked list
    # Time Complexity: O(n)
    # This is the best possible time complexity class, since we have to iterate 
    # through the whole list to search exhaustively. 
    # If we are allowed to add another pointer that points to the previous node, 
    # (i.e. a doubly linked list), the time complexity would be improved to O(1).
    # --------------------------------------------------------------------------------
    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node: 
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        return
    
    # --------------------------------------------------------------------------------
    # Displays the list in some reasonable way
    # Time Complexity: O(n)
    # This is the best possible time complexity class, since we have to iterate 
    # through the whole list to print every node. 
    # --------------------------------------------------------------------------------
    def __str__(self):
        output = ""
        curr_node = self.head
        while curr_node:
            output += str(curr_node.value) + " -> "
            curr_node = curr_node.next
        return output + "NULL"
    

if __name__ == "__main__":
    # initiate list
    SLL = LinkedList(10)
    # add nodes
    SLL.addNode(20)
    SLL.addNode(30)
    SLL.addNode(20)
    SLL.addNode(20)
    SLL.addNode(40)
    SLL.addNode(10)
    # test __str__
    print(SLL) # 10 -> 20 -> 30 -> 20 -> 20 -> 40 -> 10 -> NULL
    # add node after 
    SLL.addNodeAfter(999, SLL.head.next) # 10 -> 20 -> 999 -> 30 -> 20 -> 20 -> 40 -> 10 -> NULL
    # add node before
    SLL.addNodeBefore(888, SLL.head) # 888 -> 10 -> 20 -> 999 -> 30 -> 20 -> 20 -> 40 -> 10 -> NULL
    # remove a node
    SLL.removeNode(SLL.head.next.next.next) # 888 -> 10 -> 20 -> 30 -> 20 -> 20 -> 40 -> 10 -> NULL
    # remove nodes by value = 20
    SLL.removeNodesByValue(20) # 888 -> 10 -> 30 -> 40 -> 10 -> NULL
    # reverse the list
    SLL.reverse() # 10 -> 40 -> 30 -> 10 -> 888 -> NULL
    # check the length 
    print(SLL.length()) # 5
    print(SLL) # 10 -> 40 -> 30 -> 10 -> 888 -> NULL


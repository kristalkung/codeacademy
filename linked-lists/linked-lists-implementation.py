# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node
  
    # Add your insert_beginning and stringify_list methods below:

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    # return all the nodes in the list as a string 
    # so we can print them out in the terminal
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    
      # Define your remove_node method below:
    def remove_node(self, value_to_remove):
        # set current_node to the head_node
        current_node = self.get_head_node()

        # check if the head node is equal to the value_to_remove
        if current_node.get_value() == value_to_remove:
            # set head_node to the next node if so
            self.head_node = current_node.get_next_node()
        # otherwise:
        else:
            # traverse the linked list:
            while current_node:
                # set next_node as current_node.get_next_node()
                next_node = current_node.get_next_node()

                # if the next node's value is the value_to_remove
                if next_node.get_value() == value_to_remove:
                    # point current_node to next_node's next node
                    current_node.set_next_node(next_node.get_next_node())
                    # set current_node to None since we're done removing the value
                    current_node = None
                else:
                    # move to next node if next_node's value isn't the value_to_remove
                    current_node = next_node
  

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())
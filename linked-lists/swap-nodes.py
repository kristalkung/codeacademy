# for swapping nodes:

#######################
# NODE CLASS
#######################

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


#######################
# LINKED LIST CLASS
#######################

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
    def get_head_node(self):
        return self.head_node
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node


#######################
# SWAP NODES FUNCTION
#######################

def swap_nodes(input_list, val1, val2):
    print(f'Swapping {val1} with {val2}')

    # starting at beginning so set all node1_prev & node2_prev to None
    # set node1 & node2 to the head_node
    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node

    # edge case for if val1 & val2 are the same
    if val1 == val2:
        print("Elements are the same - no swap needed")
        return

    # while node1 is not at the end of the ll
    while node1 is not None:
        # if the value of node1 == val1, then we're at the node for val1
        if node1.get_value() == val1:
            break
        # otherwise: move onto next node.
        # set node1_prev to node1. set node1 to node1.get_next_node
        node1_prev = node1
        node1 = node1.get_next_node()

    # get node2 to the node where node2.get_value() == val2
    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    # edge case for if node1 and/or node2 traverse hits the end of the ll 
    # and either or both of them are not in the ll
    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element is not in the list")
        return

    # if node1 is at the head AKA node1_prev == None
    if node1_prev is None:
        # set input_lists's head as node2
        input_list.head_node = node2
    else:
        # otherwise: set node1_prev's next node to be node2
        node1_prev.set_next_node(node2)

    # if node2_prev is none AKA node2 is the head
    if node2_prev is None:
        # set input_list's head_node as node1
        input_list.head_node = node1
    else:
        # otherwise: set node2_prev's next node as node1
        node2_prev.set_next_node(node1)

    # create a temp var to copy node1's next node
    temp = node1.get_next_node()
    
    # set node1's next node to node2's next node
    node1.set_next_node(node2.get_next_node())

    # set node2's next node to temp
    node2.set_next_node(temp)

    
#######################
# FIND THE NTH LAST NODE
#######################


def nth_last_node(linked_list, n):
    current = None
    tail_seeker = linked_list.head_node
    count = 1
    while tail_seeker:
        tail_seeker = tail_seeker.get_next_node()
        count += 1
        if count >= n + 1:
            if current is None:
                current = linked_list.head_node
            else:
                current = current.get_next_node()
    return current

#######################
# FIND MIDDLE NODE
#######################

# concept: have two pointers; 
# 1 will be fast (moves 2x node), and
# 1 slow (moves 1x node)


def find_middle(linked_list):
    # set both pointers to be at the head_node
    fast = linked_list.head_node
    slow = linked_list.head_node

    # while we're not at the end of the ll
    while fast:
        # move up fast
        fast = fast.get_next_node()

        # if fast isn't None
        if fast:
            # move both up
            fast = fast.get_next_node()
            slow = slow.get_next_node()
    return slow



ll = LinkedList()
for i in range(10):
    ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())

"""
Time and Space Complexity:

The worst case for time complexity in swap_nodes() is if 
both while loops must iterate all the way through to the end 
(either if there are no matching nodes, 
or if the matching node is at the tail). 

This means that it has a linear big O runtime of O(n), 
since each while loop has a O(n) runtime, and constants are dropped.

There are four new variables created in the function 
regardless of the input, which means that it has a 
constant space complexity of O(1).
"""
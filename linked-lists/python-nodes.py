
# define a Node class with methods:
# set_link_node(), get_link_node, and get_value
class Node:
    # link_node should default to =None
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
    
    # the next value (link_node) should be able to be updated
    def set_link_node(self, link_node):
        self.link_node = link_node
    
    def get_link_node(self):
        return self.link_node
  
    def get_value(self):
        return self.value

# example exercise:

# Add your code below:
yacko = Node('likes to yak')
wacko = Node('has a penchant for hoarding snacks')
dot = Node('enjoys spending time in movie lots')

# set yacko to point to dot
# set dot to point to wacko
yacko.set_link_node(dot)
dot.set_link_node(wacko)

# get dot's data by going through yacko
# get wacko's data by going through dot
# DO NOT FORGET THE ()'s!
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)


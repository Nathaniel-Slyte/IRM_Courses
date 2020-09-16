""""
    Part 5: Trees

"""

"""
    General Tree Node
"""
class TreeNode:
    def __init__(self, val):
        self.value = val
        self.children = []

    def depth(self):
        if len(self.children) == 0:
            return 0
    
        return 1 + max([child.depth() for child in self.children])

"""
  Binary tree with left and right node & value

  The Node class also reprents the entire Tree, by using it as the Root node
"""
class BNode:
    def __init__(self, val):
        self.left_node : BNode = None
        self.right_node :BNode = None
        self.value = val

    def depth(self):
        depth_left  = self.left_node.depth() if self.left_node != None else 0
        depth_right = self.right_node.depth() if self.right_node != None else 0

        return 1 + max(depth_left, depth_right)

    def is_balanced(self):
        return abs(
                self.right_node.depth() if self.right_node != None else 0
                - 
                self.left_node.depth() if self.left_node != None else 0
            ) <= 1
    
    """
        Returns an array of all the children nodes and the current node
    """
    def _get_nodes(self, nodes=[]):
        if self.right_node != None:
            self.right_node._get_nodes(nodes)
        if self.left_node != None:
            self.left_node._get_nodes(nodes)
        return nodes.append(self)

    """
        Balances the tree from the current node, returns a new tree
    """
    def balance(self):
        # 1: Get all values in an array and sort the array if not called with them
        nodes = self._get_nodes()
        def node_comparator(n1 : BNode, n2 : BNode):
            if n1.value == n2.value:
                return 0
            return -1 if n1.value < n2.value else 1
        sorted(nodes, cmp=node_comparator)

        # 2: Make the middle the root node, the left side of the array is left sub tree
        left_sub = nodes[:len(nodes) //2]
        right_sub = nodes[len(nodes) //2:]
        new_root = nodes[len(new_root) // 2]


        #    right side of the array is right subtree
        # 3: Recursion
        pass
        







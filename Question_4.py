"""
Find the least common ancestor between two nodes on a binary search tree.
The least common ancestor is the farthest node from the root that is an ancestor
of both nodes. For example, the root is a common ancestor of all nodes on the
tree, but if both nodes are descendents of the root's left child, then that left
child might be the lowest common ancestor. You can assume that both nodes are in
the tree, and the tree itself adheres to all BST properties. The function
definition should look like question4(T, r, n1, n2), where Tis the tree
represented as a matrix, where the index of the list is equal to the integer
stored in that node and a 1 represents a child node, r is a non-negative integer
representing the root, and n1 and n2 are non-negative integers representing the
two nodes in no particular order. For example, one test case might be ...

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
"""

class Element(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Element(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Element(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Element(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

    return root.data


def question4(matrix, root, n1, n2):
    bst = BST(root)
    for node in matrix[root]:
        bst.insert(node)

    # insert all elements in row, starting from the last
    for row in reversed(range(len(matrix))):
        for node in matrix[row]:
            bst.insert(node)


    return lca(bst.root, n1, n2)

assert question4([[0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 2) == 1

assert question4([[0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]],
                  3,
                  1,
                  4) == 3

assert question4([[0, 1, 1],
                  [0, 0, 0],
                  [0, 0, 0]],
                  0,
                  1,
                  2) == 1

# If tests passed
print('Tests passed for question 4')


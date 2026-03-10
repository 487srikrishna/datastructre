class BST:
    def __init__(self):
        self.tree = []  # List to store the tree nodes

    def insert(self, value):
        self.tree.append(value)  # Insert the value at the end of the list
        self.tree.sort()  # Sort the list to maintain BST order

    def search(self, value):
        return value in self.tree  # Check if the value is in the list

    def inorder(self):
        print(*self.tree)  # Print the sorted list (in-order traversal)

# Example usage
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

bst.inorder()  # In-order traversal (just prints the sorted list)
print("40 found:", bst.search(40))  # Search for 40

# Nikhil Paranjape
# CSE 2050
# September 27 2019


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.key)
    return


def inorder(top):
    if top is not None:
        inorder(top.left)
        print(top.key)
        inorder(top.right)


def minvaluenode(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def deletenode(top, key):

    if top is None:
        return top

    if key < top.key:
        top.left = deletenode(top.left, key)

    elif key > top.key:
        top.right = deletenode(top.right, key)

    else:
        if top.left is None:
            temp = top.right
            top = None
            return temp

        elif top.right is None:
            temp = top.left
            top = None
            return temp

        temp = minvaluenode(top.right)
        top.key = temp.key
        top.right = deletenode(top.right, temp.key)

    return top


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


if __name__ == '__main__':
    print("Begin Assignment 2: Trees")

    print(34 * "-", "\n1a. Print post order of [ 3 , [ 1, [7], [9], [10] ], [ 15 , [20] ]]\n", 33 * "-")
    root1 = None
    root1 = insert(root1, 3)
    root1 = insert(root1, 1)
    root1 = insert(root1, 7)
    root1 = insert(root1, 9)
    root1 = insert(root1, 10)
    root1 = insert(root1, 15)
    root1 = insert(root1, 20)

    postorder(root1)

    print(34 * "-", "\n2a. Print inorder sequence of tree \n", 33 * "-")
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    inorder(root)

    print(34 * "-", "\n2b. Delete the a node 70 \n", 33 * "-")
    deletenode(root, 70)
    inorder(root)

    print(34 * "-", "\n2c. Create an insertion function to insert a node(Inserting 12, and 125) \n", 33 * "-")
    insert(root, 12)
    insert(root, 125)
    inorder(root)

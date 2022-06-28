class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.parent = None
        self.item = item
        
class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def preOrderHelper(self,temp,term):
        if temp == None:
            return
        if temp.item == term:
            self.count += 1
        self.inOrderHelper(temp.left,term)
        self.inOrderHelper(temp.right,term)


    #Print in preOrder traversal
    def preOrder(self,term):
        self.preOrderHelper(self.root,term)
        count = self.count
        return count


    def inOrderHelper(self, temp,term):
        if temp == None:
            return
        self.inOrderHelper(temp.left,term)
        if temp.item == term:
            self.count += 1
        self.inOrderHelper(temp.right,term)

    def inOrder(self,term):
        self.inOrderHelper(self.root,term)
        count = self.count
        return count

    def insertHelper(self, item, temp):
        if item < temp.item and temp.left == None:
            temp.left = Node(item)
            temp.left.parent = temp
        elif item > temp.item and temp.right == None:
            temp.right = Node(item)
            temp.right.parent = temp
        if item < temp.item:
            self.insertHelper(item, temp.left)
        elif item > temp.item:
            self.insertHelper(item, temp.right)


    def insertR(self, item):
        if self.root == None:
            self.root = Node(item)
        else:
            self.insertHelper(item, self.root)


    def insert(self, item):
        if self.root == None:
            self.root = Node(item)
        else:
            temp = self.root

            while True:
                #Break if we try to insert on left side and left is none
                if item < temp.item and temp.left == None:
                    break
                elif item > temp.item and temp.right == None:
                    break

                if item < temp.item and temp.left is not None:
                    temp = temp.left
                elif item > temp.item and temp.right is not None:
                    temp = temp.right

            if item < temp.item:
                temp.left = Node(item)
                temp.left.parent = temp
            else:
                temp.right = Node(item)
                temp.right.parent = temp


    '''
    Needs to return pointer to the successor node for the current node. 
    Should be non-recursive code.
    '''
    def searchForSuccessor(self, current_node):
        node = current_node
        if node.right is not None:
            temp = node.right
            while temp is not None:
                if temp.left is None:
                    break
                temp = temp.left
            return temp
        
        temp_two = node.parent
        while temp_two is not None:
            if node != temp_two.right:
                break
            node = temp_two
            temp_two = temp_two.parent
        return temp_two
            


    '''
    Needs to return pointer to the node containing this item value. 
    Should be non-recursive code.
    '''
    def search(self, item):
        count = 0
        if self.root.item == item:		
            count += 1
        else:
            temp = self.root
            while True:
                if item < temp.item and temp.left is not None:   
                    print('hi')   
                    temp = temp.left
                    if temp.item == item:
                        count += 1
                if item > temp.item and temp.right is not None:
                    print('hi')
                    temp = temp.right
                    if temp.item == item:
                        count += 1     

        return count



    '''Needs to delete node containing this item value
    As first step: Do a search to find the reference to this node using search.
    Successor in case of 2 children should be the highest number from left sub tree
    Needs to handle 3 cases:
    - If node has no children
    - If node has 1 child
    - If node has 2 children
    '''
    def delete(self, item):
        node = self.search(item)

        if node is not None:
            if node.left == None and node.right == None:
                if node == self.root:
                    self.root == None
                else:
                    if node.parent.left == node:
                        node.parent.left == None
                    else:
                        node.parent.right == None
                #Handle the case when no children
            elif node.left == None:
                node.parent = node.right
                node = None
                #Handle case when right child and no left children
            elif node.right == None:
                node.parent = node.left
                node = None
                #Handle case when left child and no right children
            else:
                #Handle case when 2 children:
                successor = self.searchForSuccessor(node)
                value = successor.item
                self.delete(value)
                node.item = value
                #complete the rest:


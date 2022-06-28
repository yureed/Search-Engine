class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.parent = None
        self.item = item
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def inOrderHelper(self, temp):
        if temp == None:
            return
        self.inOrderHelper(temp.left)
        print(temp.item, "Height:", temp.height)
        self.inOrderHelper(temp.right)

    def inOrder(self):
        self.inOrderHelper(self.root)

    def getHeight(self, temp):
        if temp == None:
            return 0
        else:
            return temp.height

    def leftRotation(self, node):
        print("Applying left rotation...")
        parent = node.parent
        rightChild = node.right

        node.right = rightChild.left
        if node.right is not None:
            node.right.parent = node

        rightChild.right = node
        node.parent = rightChild

        if parent is None:
            self.root = rightChild
        elif parent.right == node:
            parent.right = rightChild
        else:
            parent.right = rightChild

        rightChild.parent = parent

    def rightRotation(self, node):
        print("Applying right rotation...")
        parent = node.parent
        leftChild = node.left

        node.left = leftChild.right

        if node.left is not None:
            node.left.parent = node

        leftChild.right = node
        node.parent = leftChild

        if parent is None:
            self.root = leftChild
        elif parent.left == node:
            parent.left = leftChild
        else:
            parent.right = leftChild

        leftChild.parent = parent

    def recomputeHeight(self, temp):
        if temp is not None:
            temp.height = 1+max(self.getHeight(temp.left), self.getHeight(temp.right))

    def checkForBalance(self, temp):
        while temp is not None: #Loop to go to parent until you reach the root
            balance = self.getHeight(temp.right) - self.getHeight(temp.left)
            print("Item", temp.item, "Balance:", balance)
            if balance == -2:
                leftChild = temp.left
                leftChildBalance = self.getHeight(leftChild.right) -  self.getHeight(leftChild.left) 
                print("leftChildBalance:", leftChildBalance)
                if leftChildBalance <= 0:
                    #Right rotation:
                    self.rightRotation(temp)

                    self.recomputeHeight(temp.left)
                    self.recomputeHeight(temp.right)
                    self.recomputeHeight(temp)


                else:
                    #1. Left rotation on leftChild              
                    #2. Right rotation on temp
                    self.leftRotation(leftChild)
                    self.rightRotation(temp)
                    

                break
            elif balance == 2:
                rightChild = temp.right
                rightChildBalance = self.getHeight(rightChild.right) - self.getHeight(rightChild.left)
                print("rightChildBalance:", rightChildBalance)
                if rightChildBalance <= 0:
                    #Right rotation:
                    self.leftRotation(temp)

                    self.recomputeHeight(temp.left)
                    self.recomputeHeight(temp.right)
                    self.recomputeHeight(temp)
                else:
                    self.leftRotation(rightChild)
                    self.rightRotation(temp)
                
                break
                    
                
                    

            self.recomputeHeight(temp)

            temp = temp.parent


    def insertHelper(self, item, temp):
        if item < temp.item and temp.left == None:
            temp.left = Node(item)
            temp.left.parent = temp
            self.checkForBalance(temp)
        elif item > temp.item and temp.right == None:
            temp.right = Node(item)
            temp.right.parent = temp
            self.checkForBalance(temp)

        
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
        if self.root.item == item:		
            return self.root
        else:
            temp = self.root
            while True:
                if item < temp.item and temp.left is not None:        
                    temp = temp.left
                    if temp.item == item:
                        return temp
                if item > temp.item and temp.right is not None:
                    temp = temp.right
                    if temp.item == item:
                        return temp


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













class TrieNode:
	def __init__(self):
		self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def search(self, word):
        currentNode = self.root
        for item in word:
            if currentNode.children.get(item):
                currentNode = currentNode.children[item]
                print(currentNode.children)
            else:
                return None
        return currentNode
    
    def insert(self, word):
        currentNode = self.root
        for item in word:
            if currentNode.children.get(item):
                currentNode = currentNode.children[item]
            else:
                newNode = TrieNode()
                currentNode.children[item] = newNode
                currentNode = newNode
        currentNode.children["*"] = None




class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        
        for w in word:
            if w not in current_node.children:
                current_node.children[w] = TrieNode()
            
            current_node = current_node.children[w]
        current_node.word = True

    def search(self, word: str) -> bool:
        current_node = self.root

        for w in word:
            if w not in current_node.children:
                return False

            current_node = current_node.children[w]
        
        return current_node.word


    def startsWith(self, prefix: str) -> bool:
        current_node = self.root

        for w in prefix:
            if w not in current_node.children:
                return False

            current_node = current_node.children[w]

        return True     
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
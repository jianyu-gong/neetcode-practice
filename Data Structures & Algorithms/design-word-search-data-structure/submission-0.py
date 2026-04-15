class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root

        for w in word:
            if w not in current_node.children:
                current_node.children[w] = TrieNode()
            
            current_node = current_node.children[w]

        current_node.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):

            current_node = root

            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in current_node.children:
                        if dfs(i+1, current_node.children[child]):
                            return True
                    return False
                else:
                    if word[i] not in current_node.children:
                        return False
                    
                    current_node = current_node.children[word[i]]
            return current_node.word

        return dfs(0, self.root)
        
class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False


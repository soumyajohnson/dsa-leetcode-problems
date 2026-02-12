class TrieNode:
    def __init__(self):
        self.children={}
        self.eow=False

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        temp=self.root
        for c in word:
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
        temp.eow=True

    def search(self, word: str) -> bool:
        temp=self.root
        for c in word:
            if c not in temp.children:
                return False
            temp=temp.children[c]
        return temp.eow

    def startsWith(self, prefix: str) -> bool:
        temp=self.root
        for p in prefix:
            if p not in temp.children:
                return False
            temp=temp.children[p]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
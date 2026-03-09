class TrieNode:
    def __init__(self):
        self.children={}
        self.eow=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        temp=self.root
        for c in word:
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
        temp.eow=True

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                return node.eow
            c=word[i]
            if c=='.':
                return any(dfs(child, i+1) for child in node.children.values())
            if c not in node.children:
                return False
            return dfs(node.children[c],i+1)
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
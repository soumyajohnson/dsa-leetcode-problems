class TrieNode:
    def __init__(self):
        self.children={}
        self.sugg=[]

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        temp=self.root
        for c in word:
            if c not in temp.children:
                temp.children[c]=TrieNode()
            temp=temp.children[c]
            if len(temp.sugg)<3:
                temp.sugg.append(word)

    def startsWith(self, prefix: str) -> bool:
        temp=self.root
        for p in prefix:
            if p not in temp.children:
                return []
            temp=temp.children[p]
        return temp.sugg

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        wordTree=Trie()
        products.sort()
        for p in products:
            wordTree.insert(p)
        res=[]
        searchStr=''
        for s in searchWord:
            searchStr+=s
            res.append(wordTree.startsWith(searchStr))
        return res
        
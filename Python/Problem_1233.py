from typing import List

# Problem - 1233. Remove Sub-Folders from the Filesystem
# Python3 Solution!
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def add(self, path: str):
        cur = self
        for f in path.split('/'):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        cur.end = True
    
    def search(self, path: str):
        cur = self
        for f in path.split('/')[:-1]:
            cur = cur.children[f]
            if cur.end:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.add(f)
        res = []
        for f in folder:
            if not trie.search(f):
                res.append(f)
        return res
    
    def removeSubfolders_set_split(self, folder: List[str]) -> List[str]:
        folders_set = set(folder)
        res = []
        for f in folder:
            res.append(f)
            pre = ""
            for cur in f.split('/')[1:-1]:
                pre = pre + '/' + cur
                if pre in folders_set:
                    res.pop()
                    break
        return res
    
    def removeSubfolders_set(self, folder: List[str]) -> List[str]:
        folders_set = set(folder)
        res = []
        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i] == '/' and f[:i] in folders_set:
                    res.pop()
                    break
        return res
    
    
if __name__=="__main__":
    sol = Solution()
    
    print(sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
    print(sol.removeSubfolders(["/a","/a/b/c","/a/b/d"]))
    print(sol.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))
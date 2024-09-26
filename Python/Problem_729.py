# Problem - 729. My Calendar I
# Python3 Solution!
class BST:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, start, end) -> bool:
        cur = self
        while True:
            if end <= cur.start:
                if not cur.left:
                    cur.left = BST(start, end)
                    return True
                cur = cur.left
            elif start >= cur.end:
                if not cur.right:
                    cur.right = BST(start, end)
                    return True
                cur = cur.right
            else:
                return False

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = BST(start, end)
            return True
        return self.root.insert(start, end)
    
if __name__=='__main__':
    obj = MyCalendar()
    print(obj.book(10, 20))
    print(obj.book(15, 25))
    print(obj.book(20, 30))
# Problem - 432. All O`one Data Structure
# Python3 Solution!
class Node:
    def __init__(self, curFreq: int) -> None:
        self.freq = curFreq
        self.keys = set()
        self.prev, self.next = None, None

class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_map = {}

    def _add_node(self, cur_node: Node, freq: int) -> Node:
        new_node = Node(freq)
        new_node.prev = cur_node
        new_node.next = cur_node.next
        cur_node.next.prev = new_node
        cur_node.next = new_node
        return new_node
    
    def _remove_empty_node(self, curNode: Node) -> None:
        if not curNode.keys:
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev

    def inc(self, key: str) -> None:
        if key in self.key_map:
            cur_node = self.key_map[key]
            cur_node.keys.remove(key)

            new_freq = cur_node.freq + 1
            next_node = cur_node.next

            if next_node == self.tail or next_node.freq != new_freq:
                next_node = self._add_node(cur_node, new_freq)

            next_node.keys.add(key)
            self.key_map[key] = next_node

            self._remove_empty_node(cur_node)
        else:
            first_node = self.head.next
            if first_node == self.tail or first_node.freq != 1:
                first_node = self._add_node(self.head, 1)

            first_node.keys.add(key)
            self.key_map[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.key_map:
            return
        
        cur_node = self.key_map[key]
        cur_node.keys.remove(key)

        if cur_node.freq == 1:
            del self.key_map[key]
        else:
            new_freq = cur_node.freq - 1
            prev_node = cur_node.prev
            
            if prev_node == self.head or prev_node.freq != new_freq:
                prev_node = self._add_node(prev_node, new_freq)

            prev_node.keys.add(key)
            self.key_map[key] = prev_node

        self._remove_empty_node(cur_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


if __name__=='__main__':
    obj = AllOne()
    
    obj.inc('hello')
    obj.inc('hello')
    print(obj.getMaxKey())
    print(obj.getMinKey())
    obj.inc('leet')
    print(obj.getMaxKey())
    print(obj.getMinKey())
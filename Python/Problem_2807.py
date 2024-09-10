from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Problem - 2807: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
# Python3 Solution!
class Solution:
    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            cur.next = ListNode(self.gcd(cur.val, cur.next.val), cur.next)
            cur = cur.next.next
        
        return head
    

if __name__=="__main__":
    sol = Solution()

    input = [18, 6, 10, 3]
    head = ListNode(input[0])
    cur = head
    for i in input[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    res = sol.insertGreatestCommonDivisors(head)
    while res:
        print(str(res.val), end=' ')
        res = res.next
    print('')

    input = [7]
    head = ListNode(input[0])
    cur = head
    for i in input[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    res = sol.insertGreatestCommonDivisors(head)
    while res:
        print(str(res.val), end=' ')
        res = res.next
    print('')
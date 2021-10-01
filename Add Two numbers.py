class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        s2 = ""
        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next
        s = str(int(s1) + int(s2))
        list_s = [int(i) for i in s]
        list_s.reverse()
        if list_s:
            head = ListNode(list_s[0])
            tail = head
            for i in range(1, len(list_s)):
                head.next = ListNode(list_s[i])
                head = head.next
                
            return tail
        else:
            return ListNode()

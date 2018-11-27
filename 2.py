# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getnum(node):
            ans=0
            pow=0
            while node is not None:
                ans+=node.val*10**pow
                pow+=1
                node=node.next
            return ans
        num = str(getnum(l1)+getnum(l2)) #dealing the data in int is not efficient somehow
        #print(num)
        head = ListNode(num[-1])
        l = head
        num = num[:-1]
        while num != '':
            l.next=ListNode(num[-1])
            l=l.next
            num = num[:-1]
        return head

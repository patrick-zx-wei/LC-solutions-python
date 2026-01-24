# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        curNode = None
        tempNode = None
        if list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                newList = list1
                list1 = list1.next
            else:
                newList = list2
                list2 = list2.next
        elif list1 is not None:
            newList = list1
            list1 = list1.next
        elif list2 is not None:
            newList = list2
            list2 = list2.next

        curNode = newList
        tempNode = newList

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tempNode = list1
                list1 = list1.next
                curNode.next = tempNode
                curNode = curNode.next
                
            else:
                tempNode = list2
                list2 = list2.next
                curNode.next = tempNode
                curNode = curNode.next
        while list1 is not None:
                tempNode = list1
                list1 = list1.next
                curNode.next = tempNode
                curNode = curNode.next
        while list2 is not None:
            tempNode = list2
            list2 = list2.next
            curNode.next = tempNode
            curNode = curNode.next
        
        return newList

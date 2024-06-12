from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self,val) :
        new_node = ListNode(val)
        cur = self
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node

class Linklist:
    def __init__(self) :
        self.head = ListNode()
    
    def append(self,val) :
        new_node = ListNode(val)
        print("🐍 File: 2addtwonum/solve.py | Line: 14 | append ~ new_node.val",new_node.val)
        print("🐍 File: 2addtwonum/solve.py | Line: 15 | append ~ new_node.next",new_node.next)
        print()

        cur = self.head
        print("🐍 File: 2addtwonum/solve.py | Line: 16 | append ~ cur.val",cur.val)
        print("🐍 File: 2addtwonum/solve.py | Line: 17 | append ~ cur.next",cur.next)
        print()
        while cur.next!=None:
            print("🐍 File: 2addtwonum/solve.py | Line: 18 | append ~ cur.next",cur.next)
            cur = cur.next
            print("🐍 File: 2addtwonum/solve.py | Line: 20 | append ~ cur.val",cur.val)
        cur.next= new_node
        print("🐍 File: 2addtwonum/solve.py | Line: 22 | append ~ cur.next",cur.next)
        print()
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.val)
            elems.append(cur_node.next)
        print(elems)

    def get(self,index):
        if index>=self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next()
            if cur_idx == index: return cur_node.val
            cur_idx+=1



class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0
        i = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            i+=1

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        print("🏁 File: 2addtwonum/solve.py | Line: 114 | addTwoNumbers ~ result",result.val)
        dummyHead.next = None
        return result

node1 = ListNode(2)
node1.append(4)
node1.append(3)

node2 = ListNode(5)
node2.append(6)
node2.append(4)


ans = Solution().addTwoNumbers(l1=node1,l2=node2)
print("ans:", ans.val, ans.next.val, ans.next.next.val)


                       

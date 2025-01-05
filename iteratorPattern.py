class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None
    
    def __iter__(self):
        self.cur = self.head
        return self
    
    def __next__(self):
        if self.cur:
            value = self.cur.value
            self.cur = self.cur.next
            return value
        else:
            raise StopIteration



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

linkedList = LinkedList(head)
for value in linkedList:
    print(value)
        
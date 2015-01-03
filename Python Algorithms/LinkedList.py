from email import Header


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    

class LinkedList:
    
    def __init__ (self):
        self.hd = None
             
    
    def insert(self, item):
        node = Node (item)
        if self.hd is None:
            self.hd = node
        else:
            node.next = self.hd
            self.hd = node
            
    def isEmpty(self):
        return self.hd is None
    
    def size(self):
        curr = self.hd
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count
    
    def head(self):
        return self.hd
    
    def tail(self):
        return self.hd.next
        
    
    @classmethod
    def fromArray (self, arr):
        me = LinkedList()
        for item in arr:
            me.insert(item)
        return me
            
            
def test_LinkedList():
    a = [1,2,3]
    list1 = LinkedList.fromArray (a)
    assert list1.size() == len(a)
    assert list1.head().item == 3
    assert list1.tail().item == 2
    
    
    
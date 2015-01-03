
class Stack:
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def top(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.size() == 0
    
def test_Stack1():
    st1 = Stack()
    assert (st1.size() == 0)
    
    st1.push (1)
    assert (st1.size() == 1)
    assert (st1.top() == 1)
    
    st1.push (2)
    assert (st1.size() == 2)
    assert (st1.top() == 2)
    assert (st1.pop() == 2)
    assert (st1.top() == 1)
    assert (st1.size() == 1)
    

import Stack

"""
  Implement Queue using 2 stacks
  enqueue : Always push to stack
  dequeue : if q is available, pop from that 
            else move all stack to q
            pop from q
  
"""

class Queue:
    def __init__ (self):
        self.stack =  Stack.Stack()
        self.queue = Stack.Stack()
        
    def enqueue  (self,item):
        self.stack.push(item)
        
    def dequeue (self):
        if (not self.queue.isEmpty()):
            return self.queue.pop()
        else:
            for _ in xrange ( self.stack.size()):
                self.queue.push (self.stack.pop())
            return self.queue.pop()
        
    def isEmpty(self):
        return self.stack.isEmpty() and self.queue.isEmpty()
    
    def size(self):
        return self.stack.size() + self.queue.size()
        
    def top(self):
        if (not self.queue.isEmpty()):
            return self.queue.top()
        else:
            for _ in xrange (self.stack.size()):
                self.queue.push (self.stack.pop())
            return self.queue.top()
        
def test_Queue ():
    q1 = Queue()
    assert q1.isEmpty()
    
    q1.enqueue (1)
    q1.enqueue (2)
    assert q1.top() == 1
    assert q1.size() == 2
    
    assert (q1.dequeue() == 1)
    assert (q1.dequeue() == 2)
    
    q2 = Queue ()
    
    q2.enqueue ('A')
    assert (q2.dequeue() == 'A')
    
    assert q2.isEmpty()
    q2.enqueue ('B')
    assert q2.top() == 'B'
    q2.dequeue ()
    
    q2.enqueue ('H') ; q2.enqueue('C')
    assert q2.top() == 'H'
    assert q2.dequeue() == 'H'
    q2.enqueue ('E')
    assert q2.top() == 'C'
    
    
    
    
        
    
        
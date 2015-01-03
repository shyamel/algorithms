
from Queue import Queue


class BinTree:
    def __init__ (self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        if (left is not None):
            left.parent = self
        if (right is not None):
            right.parent = self
            
    @classmethod
    def fromArray (cls, array):
        return cls.fromArrayPart(array,0,len(array) - 1)
    
    @classmethod
    def fromArrayPart (cls, array, start, end):
        '''
        '''
        if (start == end):
            return cls(array[start], None, None)
        
        mid = (start + end) / 2
        if (mid > start):
            treeLeft = cls.fromArrayPart (array,start, mid -1)
        else:
            treeLeft = None
        if (mid +1 <= end):  
            treeRight = cls.fromArrayPart (array, mid + 1, end)
        else:
            treeRight = None
        return cls (array[mid], treeLeft, treeRight)
        
    def left_child (self):
        return self.left
    
    def right_child (self):
        return self.right
    
    def root_elem (self):
        return self.value
    
    def height (self):
        left_height = 0 if (self.left is None) else self.left.height()
        right_height = 0 if (self.right is None) else self.right.height ()
        return 1 + max (left_height, right_height)
        
    
    def inOrder (self):
        def recur (node, array):
            if (node != None):
                recur (node.left, arr)
                arr.append(node.value)
                recur (node.right, arr)
                
        arr = []
        recur (self, arr)
        return arr
    
    def preOrder (self):
        def recur (node, arr):
            if (node != None):
                arr.append (node.value)
                recur (node.left, arr)
                recur (node.right, arr)
        arr = []
        recur (self,arr)
        return arr
            
    def postOrder (self):
        def recur (node, arr):
            if (node !=None):
                recur(node.left, arr)
                recur(node.right,arr)
                arr.append (node.value)
        arr = []
        recur (self,arr)
        return arr
    
    def allPathsToLeaves (self):
        
        def recur(node, path):
            if node is not None:
                #print path, node.value
                path.append (node.value)
                if node.left is None and node.right is None:
                    allpaths.append (path)
                else:
                    if node.left is not None:
                        recur (node.left, path[:])
                    if node.right is not None:
                        recur (node.right, path)
            
        allpaths = []
        
        recur (self, [])
        
        return allpaths
        
        
    
    def allLeaves(self):
        pass
            
    
    
    def dfs (self):
        q = Queue()
        arr = []
        
        q.enqueue (self)
        
        while ( not q.isEmpty()):
            item = q.dequeue()
            arr.append (item.value)
            left = item.left
            right = item.right
            if (left is not None):
                q.enqueue (left)
            if (right is not None):
                q.enqueue (right)
                
        return arr
    
    
    def bfs (self):
        def recur (node, array):
            if node is None:
                return
            else:
                array.append (node.value)
                recur (node.left, array)
                recur (node.right, array)
        arr = []    
        recur (self, arr)
        return arr
    
    def isBalanced (self):
        """
            left subtree is balanced right subtree is balanced
            their heights differ by at most one
        """
        def heightAndBalance (node):
            if node is None:
                return (True, 0)
            leftBalance, leftHeight = heightAndBalance (node.left)
            if not leftBalance:
                return (False, None)
            
            rightBalance, rightHeight = heightAndBalance (node.right)
            if not rightBalance:
                return False, None
            
            if abs(leftHeight - rightHeight) > 1:
                return False, None
            
            return True, 1 + max (leftHeight, rightHeight)
        
        balanced, height = heightAndBalance (self)
        
        return balanced
    
    def findNode (self, key):
        def recur (node, key):
            """
                Assume search tree = true
            """
            #print node, key
            
            if node is None:
                return None
            elif node.value == key:
                return node
            elif node.value < key:
                return recur (node.right, key)
            else:
                return recur (node.left, key)
        return recur (self, key)
    
    def isBST(self):
        """
           do in order traversal
           each node must be greater than the previous one
          
        """
        
        def recurIsBST (node, maxArr):
            if node is None:
                return True
            else:
                isBST = recurIsBST (node.left, maxArr)
                if not isBST: 
                    return False
                prev = maxArr[0]
                curr = node.value
                if prev is not None and curr < prev:
                    return False
                maxArr [0] = curr
                return recurIsBST (node.right, maxArr)
                
                
            
        return recurIsBST(self, [None])
    
    def pathToKey(self, key):
        """
           If search tree
        """
        pass
        
            
           
def successor (node):
    """ Successor using parent node 
        Left most node of rightChild (if any) OR
        find first ancestor which is to right of its child
    """
    if node == None:
        return None
    else:
        if node.right is not None:
            node = node.right
            while node.left is not None:
                node = node.left
            return node
        else:   # find first parent which is to right of its child
            parent = node.parent
            while parent is not None:
                if parent.left == node:
                    return parent
                else:
                    node = parent
                    parent = node.parent
        return None
                    
            
            
def test_BinTree1 ():
    
    arr = [1]
     
    tree2 = BinTree.fromArray(arr)
     
    assert (tree2.height() == 1)
    assert (tree2.inOrder() == arr)
    assert (tree2.preOrder() == arr)
    assert (tree2.postOrder() == arr)
    
    assert tree2.findNode(1) is not None
    
    assert successor (tree2.findNode(1)) == None
    
    assert tree2.isBST()
    
    assert tree2.allPathsToLeaves() == [[1]]
    
    
def test_BinTree2():
    
    arr = [1,2]
     
    tree2 = BinTree.fromArray(arr)
     
    assert (tree2.height() == 2)
    assert (tree2.root_elem() == 1)
    assert (tree2.inOrder() == arr)
    assert (tree2.preOrder() == [1,2])
    assert (tree2.postOrder() == [2,1])
    assert (tree2.dfs() == [1,2])
    assert (tree2.bfs() == [1,2])
    assert tree2.isBalanced()
    assert successor(tree2.findNode(1)) == tree2.findNode(2)
    
    assert tree2.isBST()
    
    assert tree2.allPathsToLeaves() == [[1,2]]

    
def test_BinTree3():
    
    arr = [1,2,3]
     
    tree2 = BinTree.fromArray(arr)
     
    assert (tree2.height() == 2)
    assert (tree2.inOrder() == arr)
    assert (tree2.preOrder() == [2,1,3])
    
    assert (tree2.postOrder() == [1,3,2])
    assert (tree2.dfs() == [2,1,3])
    assert (tree2.bfs() == [2,1,3])
    
    assert (tree2.isBalanced())
    
    assert successor(tree2.findNode(1)) == tree2.findNode(2)
    assert successor(tree2.findNode(2)) == tree2.findNode(3)
    assert successor(tree2.findNode(3)) == None
    
    assert tree2.isBST()
    
    assert tree2.allPathsToLeaves() == [[2,1], [2,3]]
    
    arr = [1,2,3,4,5]
    
    tree3 = BinTree.fromArray(arr)

    
    
    assert tree3.allPathsToLeaves() == [[3,1,2], [3,4,5]]
    
    
    arr = [1,2,3,4,5,6,7]
    
    tree4 = BinTree.fromArray(arr)
    
    assert tree4.allPathsToLeaves() == [[4,2,1], [4,2,3], [4,6,5], [4,6,7] ]

    
def test_Bintree4():
    
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    tree = BinTree.fromArray (arr)
    assert (tree.height() == 5)
    
    assert (tree.inOrder() == arr)
    assert (tree.root_elem() == 11)
    
    assert tree.isBalanced()
    
    for i in xrange (1, 21):
        nodeI = tree.findNode(i)
        assert nodeI.value == i
        succI = successor (nodeI)
        assert succI is not None
        assert succI == tree.findNode(i + 1)
    assert successor (tree.findNode(21)) is None
    
    assert tree.isBST()
    
    assert tree.allPathsToLeaves() == [1]
    
def test_isBST ():
    
    tree = BinTree.fromArray ([1,2])
    assert tree.isBST()
    tree = BinTree.fromArray ([1,3,2])
    assert not tree.isBST()
    


    
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    tree = BinTree.fromArray (arr)
    assert tree.isBST()
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,17,19,20,21]
    tree = BinTree.fromArray (arr)
    assert not tree.isBST()
    
    arr = [2,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    tree = BinTree.fromArray (arr)
    assert not tree.isBST()
    
    
    
    

""" 
Data structures implemented for demo use
Node
NodeDeque 
"""
        
class NodeDeque(object):
    def __init__(self):
        self.head, self.tail = None, None
        
    def append(self, nd):
        """ append a node to deque """
        if not self.isNode(nd):
            raise TypeError("Should add a Node, not a NodeDeque")
        if not self.empty():
            self.tail.nxt, nd.prev = nd, self.tail
            self.tail = nd
        else:
            self.head = nd
            self.tail = nd
                       
    def index(self, idx):
        """ get deque[idx] """
        # 1. exceptions
        if self.empty():
            raise IndexError("NodeDeque is empty")
        # 2. locate deque[idx]
        if idx < 0:
            curr = self.tail
            while idx < -1: # reversing
                try:
                    curr = curr.prev
                except Exception:
                    raise IndexError("Invalid index")    
                idx += 1
        else:
            curr = self.head
            while idx > 0: # heading
                try:
                    curr = curr.nxt
                except Exception:
                    raise IndexError("Invalid index") 
                idx -= 1  
        return curr
    
    @staticmethod
    def isNode(nd):
        """ 
        some node may have predecessor/successor,
        return True if nd is "single"  
        """
        return nd.nxt == None and nd.prev == None    
     
    def insert(self, nd, idx=-1):
        """ 
        reverse operation of remove 
        add a node after deque[idx]
        """
        # 1. Validate nd
        if not self.isNode(nd):
            raise TypeError("Should add a Node, not a NodeDeque")
        # 2. Locate deque[idx]
        try:
            curr = self.index(idx)
        except IndexError: # deque is empty
            self.head = nd
            self.tail = nd
            return
        # 3. Append nd to curr
        curr.nxt, nd.prev = nd, curr
        if curr == self.tail:
            self.tail = nd                  
           
    def empty(self):
        return self.head == None    
    
    def remove(self, idx=-1):
        # 1. Locate deque[idx]
        curr = self.index(idx)               
        # 2. Remove references to and from curr, reorganize deque
        if self.head == self.tail: # single element in deque
            self.head, self.tail = None, None
            curr.prev, curr.nxt  = None, None                
        elif curr == self.tail: # pop last element
            curr.prev.nxt = None
            self.tail = curr.prev
            curr.prev, curr.nxt  = None, None
        elif curr == self.head: # pop first element
            curr.nxt.prev = None
            self.head = curr.nxt
            curr.prev, curr.nxt  = None, None
        else: # middle elements case
            curr.prev.nxt = curr.nxt
            curr.nxt.prev = curr.prev
            curr.prev, curr.nxt  = None, None                                  
                    
    def pop(self):
        if self.empty():
            raise Exception("NodeDeque is empty")
        curr = self.tail
        curr.prev.nxt = None
        self.tail = curr.prev
        curr.prev = None
        return curr
               
    def __repr__(self):
        curr = self.head
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.nxt
        return ("NodeDeque%r" % lst)
                



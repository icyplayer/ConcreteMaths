"""
Data structures implemented for demo use
ListDeque
NodeDeque

"""


class DequeBase(object):
    def __init__(self):
        pass

    def __len__(self):
        pass

    def append(self, nd):
        pass

    def index(self, idx):
        pass

    def insert(self, nd, idx=-1):
        pass

    def empty(self):
        pass

    def remove(self, idx=-1):
        pass

    def pop(self):
        pass
    
    def peek(self):
        pass


class NodeDeque(DequeBase):
    def __init__(self):
        self.head, self.tail = None, None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, nd):
        """ append a node to deque """
        if not self.isElement(nd):
            raise TypeError("Should add a Node, not a NodeDeque")
        if not self.empty():
            self.tail.nxt, nd.prev = nd, self.tail
            self.tail = nd
        else:
            self.head = nd
            self.tail = nd
        self.length += 1

    def index(self, idx):
        """ get deque[idx] """
        # 1. exceptions
        if self.empty():
            raise IndexError("NodeDeque is empty")
        # 2. locate deque[idx]
        if idx < 0:
            curr = self.tail
            while idx < -1:  # reversing
                try:
                    curr = curr.prev
                except Exception:
                    raise IndexError("Invalid index")
                idx += 1
        else:
            curr = self.head
            while idx > 0:  # heading
                try:
                    curr = curr.nxt
                except Exception:
                    raise IndexError("Invalid index")
                idx -= 1
        return curr

    @staticmethod
    def isElement(nd):
        """
        some node may have predecessor/successor,
        return True if nd is "single"
        """
        return nd.nxt is None and nd.prev is None

    def insert(self, nd, idx=-1):
        """
        reverse operation of remove
        add a node after deque[idx]
        """
        # 1. Validate nd
        if not self.isElement(nd):
            raise TypeError("Should add a Node, not a NodeDeque")
        # 2. Locate deque[idx]
        try:
            curr = self.index(idx)
        except IndexError:  # deque is empty
            self.head = nd
            self.tail = nd
            return
        # 3. Append nd to curr
        curr.nxt, nd.prev = nd, curr
        if curr == self.tail:
            self.tail = nd
        self.length += 1

    def empty(self):
        return self.head is None

    def remove(self, idx=-1):
        # 1. Locate deque[idx]
        curr = self.index(idx)
        # 2. Remove references to and from curr, reorganize deque
        if self.head == self.tail:  # single element in deque
            self.head, self.tail = None, None
        elif curr == self.tail:  # pop last element
            curr.prev.nxt = None
            self.tail = curr.prev
        elif curr == self.head:  # pop first element
            curr.nxt.prev = None
            self.head = curr.nxt
        else:  # middle elements case
            curr.prev.nxt = curr.nxt
            curr.nxt.prev = curr.prev
        curr.prev, curr.nxt = None, None
        self.length -= 1

    def pop(self):
        if self.empty():
            raise Exception("NodeDeque is empty")
        curr = self.tail
        curr.prev.nxt = None
        self.tail = curr.prev
        curr.prev = None
        self.length -= 1
        return curr
    
    def peek(self):
        if self.empty():
            raise IndexError("NodeDeque is empty")
        return self.head

    def __repr__(self):
        curr = self.head
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.nxt
        return ("NodeDeque%r" % lst)


class ListDeque(DequeBase):
    """ Deque implemented using Python built-in list """
    def __init__(self):
        self.lst = []

    def __len__(self):
        return len(self.lst)

    def append(self, x):
        """ append a element x to deque """
        self.lst.append(x)

    def index(self, idx):
        """ get deque[idx] """
        return self.lst[idx]

    @staticmethod
    def isElement(x):
        """
        some node may have predecessor/successor,
        return True if x is "single"
        """
        return not isinstance(x, list)

    def insert(self, x, idx=-1):
        """
        reverse operation of remove
        add an element after deque[idx]
        """
        return self.lst.insert(idx, x)

    def empty(self):
        return len(self.lst) == 0

    def remove(self, idx=-1):
        try:
            if idx < 0:
                while idx < -1:
                    self.lst[idx] = self.lst[idx+1]
                    idx += 1
            else:
                oldLen = len(self.lst)
                for i in range(idx+1, oldLen):
                    self.lst[i-1] = self.lst[i]
            self.lst.pop()
        except Exception:
            raise Exception("remove error")

    def pop(self):
        return self.lst.pop()

    def __repr__(self):
        return ("ListDeque%r" % self.lst)
    
    def peek(self):
        if self.empty():
            raise IndexError("ListDeque is empty")        
        return self.lst[0]

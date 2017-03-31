"""
Created on 2017年3月30日

@author: ipr
"""

class Node(object):
    def __init__(self, val):
        self.nxt = None
        self.prev = None
        self.val = val
    
    def __repr__(self, *args, **kwargs):
        return "Node(%s)" % str(self.val)
    
    def value(self):
        return self.val
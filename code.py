class LTree:
    def __init__(self,arr,merge = max):
        self.arr = arr
        self.merge = merge
        self.root = self.Node(0,len(arr),self)
    def find(self,l,r):
        return self.root.find(l,r)
    def update(self,idx,v):
        self.arr[idx] = v
        self.root.update(idx,v)
    class Node:
        def __init__(self,l,r,outer):
            self.l,self.r = l,r
            self.outer = outer
            if l == r:
                self.v = outer.arr[l]
            else:
                mid = (l + r) // 2
                self.lc,self.rc = outer.Node(l,mid,outer),outer.Node(mid + 1,r,outer)
                self.v = outer.merge(self.lc.v,self.rc.v)
        def find(self,l,r):
            if self.l == l and self.r == r:
                return self.v
            mid = (l + r) // 2
            if r <= mid:
                return self.lc.find(l,r)
            elif l > mid:
                return self.rc.find(l,r)
            else:
                return self.outer.merge(self.lc.find(l,mid),self.rc.find(mid + 1,r))
        def update(self,idx,v):       
            if idx == self.l == self.r:
                self.v = v
            else:
                mid = (self.l + self.r) // 2
                if idx <= mid:
                    self.lc.update(idx,v)
                else:
                    self.rc.update(idx,v)
                self.v = self.outer.merge(self.lc.v,self.rc.v)

class HuffTree:
    def __init__(self, p, symbol='', left=None, right=None):
        self.p = p
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

    def setCodes(self, code=''):
        self.code = code
        if (self.left):
            self.left.setCodes(code+"1")
        if (self.right):
            self.right.setCodes(code+"0")

    def getLeaves(self, action):
        if (self.left):
            self.left.getLeaves(action)
        if (self.right):
            self.right.getLeaves(action)
        else:
            action(self)

class BST:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = BST(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = BST(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals


a = BST()
print('Menu')
print('1.insert')
print('2.preorder')
print('3.inorder')
print('4.postorder')
print('5.break')

while(True):
    ch = int(input('Enter your choice:'))
    if(ch == 1):
        data = int(input('Enter the element:'))
        a.insert(data)
    elif(ch == 2):
        print('PREORDER', a.preorder([]))
    elif(ch == 3):
        print('INORDER', a.inorder([]))
    elif(ch == 4):
        print('POSTORDER', a.postorder([]))
    elif(ch == 5):
        break
    else:
        print('Invalid choice')
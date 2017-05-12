'''She Codes lesson 11 exercise 6.'''
#Very primitive implementation of BST :-/

hop = 0


class TreeNode():
    def __init__(self, parent=None):
        self.parent = parent
        self.leftChild = None
        self.rightChild = None

    def insert(self, key):
        if not self.parent:
            Root.root = Root(key)
            self.parent = key
        elif self.parent > key:
            if not self.leftChild:
                self.leftChild = TreeNode(key)
                return self.leftChild
            else:
                return self.leftChild.insert(key)
        elif self.parent < key:
            if not self.rightChild:
                self.rightChild = TreeNode(key)
                return self.rightChild
            else:
                return self.rightChild.insert(key)
        else:
            return False

    def lookup(self, key):
        global hop
        if self.parent:
            hop += 1
            if self.parent == key:
                print('Good ', key, 'hops:', hop)
                hop = 0
            elif self.parent > key and self.leftChild:
                return self.leftChild.lookup(key)
            elif self.parent < key and self.rightChild:
                return self.rightChild.lookup(key)
            else:
                return False
        else:
            return False


class Root(TreeNode):
    def __init__(self, root=None):
        self.root = root
        # self.parent = None


new_member = TreeNode()
new_member.insert(101)
new_member.insert(20)
new_member.insert(10)
new_member.insert(2)
new_member.insert(1)
new_member.insert(200)
new_member.insert(125)
new_member.insert(101)
# new_member.lookup(101)
# new_member.lookup(120)
# new_member.lookup(125)
new_member.lookup(2)
new_member.lookup(200)
print (new_member.lookup(500))
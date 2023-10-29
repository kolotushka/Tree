class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def create_tree(self, obj):
        if self.root:
            self.check(obj)

        if not self.root:
            self.root = obj

    def check(self, obj):
        a = self.root
        while a != None:
            if obj.data > a.data:
                if a.right == None:
                    a.right = obj
                    break
                a = a.right
            if obj.data < a.data:
                if a.left == None:
                    a.left = obj
                    break
                a = a.left

    def show(self):
        v = [self.root]
        while v:
            lst = []
            for q in v:
                print(q.data)
                if q.left:
                    lst.append(q.left)
                if q.right:
                    lst.append(q.right)
            v = lst


a = [7, 9, 5, 6, 4, 11, 8]
t = Tree()
for q in a:
    t.create_tree(Node(q))

t.show()


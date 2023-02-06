class pQueue():
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, data):
        self.queue.append(data)
    
    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def printInorder(root):

    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

def printPostorder(root):
    
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

def printPreorder(root):
        
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

def printLevelOrder(root):

    if root is None:
        return

    queue = []
    queue.append(root)

    while(len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

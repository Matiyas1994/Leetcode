# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized = []
        queue = deque()
        queue.append(root)
        
        
        while queue:
            node = queue.popleft()
            
            if not node:
                serialized.append("N")
            
            else:
                serialized.append(str(node.val))
                
                queue.append(node.left)
                queue.append(node.right)
                
        return " ".join(serialized)
     
    def deserialize(self, serialized):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = list(serialized.split())
        
        for i in range(len(tree)):
            if tree[i] != "N":
                tree[i] = TreeNode(int(tree[i]))
            else:
                tree[i] = None
        j = 1
        for i  in range(len(tree)-2):
            if not tree[i]: continue
            tree[i].left = tree[j]
            tree[i].right = tree[j+1]
            j +=2
        return tree[0]
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
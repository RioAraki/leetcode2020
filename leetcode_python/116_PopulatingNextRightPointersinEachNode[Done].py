# 2019-01-02: pass

# similar recursion to 115
# everytime there is a left child, point to right child
# everytime there is a right child, point to the parent sibling's left child, deal with all right child recursively

def connect(self, root):
    if root:
        if root.left and root.right:
            root.left.next = root.right

        self.connect(root.left)
        self.connect(root.right)

        sibling = root.next

        while root.right:
            if not sibling:
                root.right.next = None
            else:
                root.right.next = sibling.left
                sibling = sibling.left
            root = root.right
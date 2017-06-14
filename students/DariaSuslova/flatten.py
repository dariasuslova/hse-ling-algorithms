def flatten(root):
    if root:
        self.flatten(root.right)
        if root.left:
            self.flatten(root.left)
            p = root.left
            while p.right is not None:
                p = p.right
            p.right, root.right, root.left = root.right, root.left, None

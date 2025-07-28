class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        # Helper: Check if node is a leaf
        def is_leaf(node):
            return node and not node.left and not node.right

        # Collect left boundary (excluding leaves)
        def get_left_boundary(node):
            left_boundary = []
            while node:
                if not is_leaf(node):
                    left_boundary.append(node.val)
                node = node.left if node.left else node.right
            return left_boundary

        # Collect right boundary (excluding leaves)
        def get_right_boundary(node):
            right_boundary = []
            while node:
                if not is_leaf(node):
                    right_boundary.append(node.val)
                node = node.right if node.right else node.left
            return right_boundary[::-1]  # Reverse for correct order

        # Collect all leaves (in-order)
        def get_leaves(node):
            if not node:
                return []
            if is_leaf(node):
                return [node.val]
            return get_leaves(node.left) + get_leaves(node.right)

        # Build the boundary
        if is_leaf(root):  # Single-node tree
            return [root.val]

        left_boundary = get_left_boundary(root.left)
        leaves = get_leaves(root)
        right_boundary = get_right_boundary(root.right)

        return [root.val] + left_boundary + leaves + right_boundary

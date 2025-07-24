class Solution:
    def distanceK(self, root, target, k):
        from collections import deque
        
        # Step 1: Build child -> parent mapping
        parent = {}
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                parent[node.left] = node
                q.append(node.left)
            if node.right:
                parent[node.right] = node
                q.append(node.right)
        
        # Step 2: BFS from target (level-order expansion)
        seen = {target}
        q = deque([(target, 0)])
        res = []
        while q:
            node, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            elif dist < k:
                for nei in (node.left, node.right, parent.get(node)):
                    if nei and nei not in seen:
                        seen.add(nei)
                        q.append((nei, dist + 1))
        return res

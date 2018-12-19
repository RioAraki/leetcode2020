# 2018-12-19: pass, 48 ms
# 2018-12-19: may want to redo the better solution

# logic:
# false as long as there is a null before any nodes with number?
# in other words, it is BFS, if None is found in the middle of BFS return False
def isCompleteTree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    queue = [root]
    out = []
    
    while len(queue) != 0:
        
        cur = queue.pop(0)
        
        if cur == None:
            out.append(None)
            continue
        else:
            out.append(cur.val)
            
        
        if cur.left:
            queue.append(cur.left)
        else:
            queue.append(None)
        
        if cur.right:
            queue.append(cur.right)
        else:
            queue.append(None)
            
    for i,j in zip(out[:-1], out[1:]):
        if i == None and j != None:
            return False
    return True

# better solution:

# bfs level order traversal, the idea is excatly the same: no empty node before any non-empty node
# implementation: instead of pop from list, he just loop through the list and check whether there will be non empty node after meeting the first empty node

def isCompleteTree(root):
    bfs = [root]
    i = 0
    # stop iteration after meeting the first None
    while bfs[i]:
        bfs.append(bfs[i].left)
        bfs.append(bfs[i].right)
        # there would always be two append after one iteration, so it will never out of index
        i += 1
    # after meeting the first None, if we find the elements after contains number node (so any[bfs[i:] would return true]) the whole thing returns false
    return not any(bfs[i:])

# conclusion: smart idea using queue, understand the property of complete tree well


# better and faster solution:

def isCompleteTree(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # use deque to form a queue rather than list
    q = collections.deque([root])
    need_leaf = False
    
    while q:
        node = q.popleft()

        # case 1: have both children
        if node.left and node.right:
            if need_leaf:
                return False
            
            q.append(node.left)
            q.append(node.right)

        # case 2: have left but no right child   
        elif node.left and node.right is None:
            # this state is allowed to happen once like the scenario [1,2,3,4], but if we have case2 or case 4 before, it cannot happen again
            if need_leaf:
                return False
            need_leaf = True
            q.append(node.left)

        # case 3：have right but no left
        elif node.left is None and node.right:
            # anytime there is right child but no left child it must be false
            return False
        # case 4: already a leaf, it does not return false even we have a need_leaf state before
        else:
            need_leaf = True
        
    return True            
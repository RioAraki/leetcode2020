# 2019-01-04: Pass, very inefficient

# bfs to traverse all nodes

# if left, try to connect to right
	# if failed, try to connect to parent's sibling's left, then right recursivly

def connect(self, root):
    
    bfs = collections.deque()
    bfs.append(root)
    
    while len(bfs):
        root = bfs.popleft()
        
        if root:
            sibling = root.next
            if root.left:
                bfs.append(root.left)
                if root.right:
                    print(root.left.val, "->", root.right.val)
                    root.left.next = root.right
                else:
                    while sibling:

                        if sibling.left:
                            print(root.left.val, "->", sibling.left.val)
                            root.left.next = sibling.left
                            break
                        elif sibling.right:
                            print(root.left.val, "->", sibling.right.val)
                            root.left.next = sibling.right
                            break
                        elif not sibling.left and not sibling.right:
                            sibling = sibling.next
                    if not sibling:
                        print(root.left.val, "->", "None")
                        root.left.next = None
            if root.right:
                bfs.append(root.right)
                while sibling:

                    if sibling.left:
                        print(root.right.val, "->",sibling.left.val)
                        root.right.next = sibling.left
                        break
                    elif sibling.right:
                        print(root.right.val, "->", sibling.right.val)
                        root.right.next = sibling.right
                        break
                    else:
                        sibling = sibling.next

                if not sibling:
                    print(root.right.val, "->", "None")
                    root.right.next = None

# [REDO] very smart and elegant bfs, regard the tree based on depth

def connect(self, root):
	# initate empty tree
    prekid = kid = TreeLinkNode(0)
    # loop through all depth
    while root:
    	# loop each depth
        while root:
            kid.next = root.left
            # if left exists, set kid to left, else remain unchanged
            kid = kid.next or kid

            # link left to right
            kid.next = root.right
            kid = kid.next or kid

            # do this recursively so that same level's nodes connect together
            root = root.next

        # root becomes the first node in next level
        # kid becomes empty tree node
        root, kid = prekid.next, prekid
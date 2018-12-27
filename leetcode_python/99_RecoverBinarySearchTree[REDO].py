#2018-12-26: need to redo, also it is not fast enough

# in order traverse, output should be sorted.
# use pred and first to record when output is not sorted
# there should be two times output is not sorted, record the nodes and change their value



def inorderIter(root):
    if root:
        for node in inorderIter(root.left): 
            yield node
        yield root        
        for node in inorderIter(root.right): 
            yield node

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        pred, first = None, None
        for node in inorderIter(root):
            print("node: ",node.val)
            if pred and pred.val > node.val:
                print("pred: ",pred.val)
                if first == None:
                    first = pred
                    second = node
                else:
                    second = node
                    break
            pred = node

        first.val, second.val = second.val, first.val
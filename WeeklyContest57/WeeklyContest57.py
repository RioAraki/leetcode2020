# Q4 https://leetcode.com/problems/candy-crush/description/

 class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # 1. detect grids with same value horizontally or vertically, eliminate them (there might be several groups)
        # Hard: wired shape detect, they must be connect with length/ width >= 3
        
        # Algorithm: iterate each grid, try to find if there are 3+ same value grid horizontally/ vertically, if there is, put all of them in a list that is going to be eliminated, we no longer to iterate those grids as well.
        def crushDetect(board):
            # detect up/down/left/right direction for same value grid, some detection could be ignored in corner case
            for w in board:
                for grid in board[w]:
                    if w > 1:
                        if board[w-1][grid] == board[w-2][grid] == board[w][grid]:
                            
        
        
        # helper, simply check three grids are same or not
        def sameValue(board)   
        # 2. move down grids above the eliminated grids in a bottom up order, leave 0 on the original positon
        # 3. run recursively until the state is stable
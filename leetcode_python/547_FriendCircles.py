def findCircleNum(M: List[List[int]]) -> int:
    # store a list with len = # of student, each element = 0 (on belongs to friend cycle of itself) or 1 (belongs to friend circle of others)

    # take a student's index as input, return all students that in this student's friend circle.
    def findAllFriends(idx):
        queue = [idx]
        
        while queue:
            cur = queue.pop(0)
            for i in range(len(M[cur])):
                if M[cur][i] == 1:                        
                    if i not in queue and friend[i] == 0:  
                        queue.append(i)
                    friend[i] = 1
        
    n = len(M)
    friend = [0 for _ in range(n)]

    ret = 0
    # loop through each student
    for i in range(n):
        # find friend cycle of that student if not in other people's friend cycle
        if friend[i] == 0:
            friend[i] = 1
            ret += 1
            friends = findAllFriends(i)

        # skip if the student is in friend cycle of other people
    return ret
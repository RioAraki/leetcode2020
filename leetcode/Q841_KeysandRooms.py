class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # We always have the key x before room x is reached

        keys = []
        visited = [0]

        for key in rooms[0]:
            if key not in visited and key not in keys:
                keys.append(key)

        while len(keys) != 0:
            nxt = keys.pop(0)
            visited.append(nxt)
            for key in rooms[nxt]:
                if key not in visited and key not in keys:
                    keys.append(key)

        return len(visited) == len(rooms)

    # Error 1: syntax error: Wrong way to init set, must be var = set()
    # Error 2: Wrong intepretation: dont understand the question, forgot we dont need to go through room one by one
    # Error 3: dummy error: used built in keyword next as variable name
    # Error 4: syntax error: use pop[0] but should be pop(0)
    # Error 5: corner case: forgot to do the same key check for first room
class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        ret = 0
        stationUsed = 0
        expectation = startFuel + stationUsed

        while expectation < target:
            forward = list(filter(lambda x: x[0] <= expectation and x[0] > stationUsed, stations))
            if len(forward):
                best = max(forward, key=lambda x: x[1])
            else:
                return -1
            print(expectation, best)
            expectation += best[1]
            stationUsed = best[0]
            ret += 1
        return ret

    # Forgot to consider the situation I need to add gas at multiple gas station to reach the final destination
    # The idea of using greedy algorithm is wrong


# Better solution with dp

# saved data dp means max distance it could reach with t's number of refuel
class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        dp = [startFuel] + [0] * len(stations)

        for i in range(len(stations)):
            for t in range(i + 1)[::-1]:
                print(t, i)
                if dp[t] >= stations[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + stations[i][1])
        for t, d in enumerate(dp):
            if d >= target: return t
        return -1
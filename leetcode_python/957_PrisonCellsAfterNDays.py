
# logic
# 1. simulation: follow the description and simulate the whole N days process, O(N)

# 2. find the **pattern** that could predict exactly what happens at the Nth day -> repeat
def prisonAfterNDays(self, cells, N):
    N -= max(N - 1, 0) // 14 * 14
    for i in range(N):
        cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
    return cells

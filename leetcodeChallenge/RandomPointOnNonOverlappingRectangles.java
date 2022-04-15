// 很有启发，说几点:
// 1. 因为不同rect面积不同，涵盖的integer point个数不同，所以不能随机选rect，大的rect选中比例大，要根据面积决定比例
// 2. 1*1 面积的 rect 能容纳 4 个点，2*2面积的rect能容纳9个点，要按照点的比例算
// 3. random pick number 只需要1次就够了，这一次已经包含了它会在哪个rect里，以及是rect的哪个点



class Solution {
    
    private int[][] rects;
    private Random r = new Random();
    private TreeMap<Integer, Integer> map = new TreeMap<>();
    private int area = 0;
    
    
    public Solution(int[][] rects) {
        this.rects = rects;
        for (int i = 0; i < rects.length; i++) {
            area += (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1);
            map.put(area, i);
        }
    }
    
    public int[] pick() {
        int randInt = r.nextInt(area);
        int key = map.higherKey(randInt);
        int[] rect = rects[map.get(key)];
        int x = rect[0] + (key - randInt - 1) % (rect[2] - rect[0] + 1);
        int y = rect[1] + (key - randInt - 1) / (rect[2] - rect[0] + 1);
        return new int[]{x, y};
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.pick();
 */
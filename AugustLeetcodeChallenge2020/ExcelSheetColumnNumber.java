class Solution {
    public int titleToNumber(String s) {
        int len = s.length();
        int sum = 0;
        int cnt = 1;
        for (char c : s.toCharArray()) {
            int cur = Character.getNumericValue(c) - 9;
            sum += cur * Math.pow(26, len - cnt);
            cnt += 1;
        }
        return sum;
    }
}
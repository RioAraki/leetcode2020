class Solution {
    public int longestPalindrome(String s) {
        int cnt = 0;
        Set<Character> chSet = new HashSet<Character>();
        for (char ch : s.toCharArray()) {
            if (!chSet.contains(ch)) {
                chSet.add(ch);
            } else {
                chSet.remove(ch);
                cnt += 2;
            }
        }
        if (!chSet.isEmpty()) {
            cnt += 1;
        }
        return cnt;
    }
}
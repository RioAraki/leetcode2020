class Solution {
    public boolean isPowerOfFour(int num) {
        // keep divide the num recursively, if the at any time result is not int, return false
        // if the return 1 return true
        if (num == 0) {
            return false;
        } else if (num == 1) {
            return true;
        } else if ((double)num / 4 == Math.floor((double)num / 4) ) {
            return isPowerOfFour((int) num / 4);
        }
        return false;
    }
}
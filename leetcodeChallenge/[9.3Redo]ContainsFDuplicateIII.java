class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        int p = 0;
        if (nums.length == 0) return false;
        if (k==0) return false;
        
        TreeSet<Long> set = new TreeSet<>(); // all numbers in the window are saved in this set
        for (int i = 0; i < nums.length; i++) {
            Long tmp1 = set.ceiling((long) nums[i]); // try to find smallest num bigger than num[i]
            Long tmp2 = set.floor((long) nums[i]);   // try to find biggest num smaller than num[i]
            if (tmp1 != null && tmp1 - nums[i] <= t) return true;
            if (tmp2 != null && nums[i] - tmp2 <= t) return true; 
            
            if (set.size() == k) set.remove((long)nums[p++]); // set is full, remove the first element
            set.add((long)nums[i]); // add the new element
        }
        return false;
    }
}
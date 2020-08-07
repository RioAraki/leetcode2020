class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        HashSet<Integer> nonDuplicate = new HashSet<Integer>();
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        for (int num : nums) {
            if (nonDuplicate.contains(num)) {
                result.add(num);
            } else {
                nonDuplicate.add(num);
            }
        }
        
        return result;
    }
}
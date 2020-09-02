// this solution uses the property that search in hashset is O(1), so overall runtime is O(n)
// but it still requires extra O(n) space

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

// rearrange number
// We can do it because we know the list should be consecutive number start from 1
// swap until index matches number or duplicate
// after finalize rearrange, check which index does not match the number
class Solution {
    public void traverse(TreeNode root, int X, int Y, HashMap<Integer, Map<Integer, List<Integer>>> map){
        if(root == null) return ;
        if(!map.containsKey(X))
            map.put(X, new HashMap<>());
        if(!map.get(X).containsKey(Y))
            map.get(X).put(Y, new ArrayList<>());
        map.get(X).get(Y).add(root.val);
        traverse(root.left, X - 1, Y + 1, map);
        traverse(root.right, X + 1, Y + 1, map);
    }
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        
        HashMap<Integer, Map<Integer, List<Integer>>> map = new HashMap<>();
        traverse(root, 0, 0, map);
        List<Integer> set = new ArrayList<>(map.keySet());
        Collections.sort(set);
        for(Integer key : set){
            
            Map<Integer, List<Integer>> temp = map.get(key);
            List<Integer> pos = new ArrayList<>(temp.keySet());
            Collections.sort(pos);
            List<Integer> t = new ArrayList<>();
            for(Integer Y : pos){
                Collections.sort(temp.get(Y));
                t.addAll(temp.get(Y));
            }
            ans.add(t);
        }
        return ans;
    }
}
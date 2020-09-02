class Solution {
    
    
    public String largestTimeFromDigits(int[] A) {
        String res = "";
        String s = "";
        List<String> permutations = new ArrayList();
        for (int a : A) {
            s += a;
        }
        permutation(s, "", permutations);
        
        
        for (String p : permutations) {
            String HH = p.substring(0, 2);
            String MM = p.substring(2);
            if (HH.compareTo("24") < 0 && MM.compareTo("60") < 0 && res.compareTo(HH + ":" + MM) < 0) {
                res = HH + ":" + MM;
            }
        }
        return res;
    }
    
    private void permutation(String s, String sofar, List<String> list) {
        if (s.isEmpty()) {
            list.add(sofar);
        }
        for (int i = 0; i < s.length(); i++) {
            permutation(s.substring(0,i) + s.substring(i + 1), sofar + s.charAt(i), list);
        }
    }
}
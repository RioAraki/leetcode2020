class Solution {
    Set<Integer> result = new HashSet<Integer>();
    
    public int[] numsSameConsecDiff(int N, int K) {
        if (N == 1) {
            return new int[]{0,1,2,3,4,5,6,7,8,9};
        }
        
        helper(N,K,new ArrayList<Integer>());
        int len = result.size();
        int[] realResult = new int[len];
        Iterator<Integer> it = result.iterator();
        int i = 0;
        while (it.hasNext()){
            realResult[i] = it.next();
            i += 1;
        }
        return realResult;
    }
    
    public void helper(int N, int K, ArrayList<Integer> temp) {
        if (temp.size() == N) {
            result.add(list2int(temp));
        } else if (temp.size() == 0) {
            for (int i = 1; i < 10; i ++) {
                helper(N, K, new ArrayList<>(Arrays.asList(i)));
            }  
        } else if (temp.size() < N) {
            ArrayList<Integer> t = (ArrayList) temp.clone();
            if (temp.get(temp.size() - 1) - K >= 0) {
                temp.add(temp.get(temp.size() - 1) - K);
                helper( N, K, temp);
            } 
            if (t.get(t.size() - 1) + K <= 9) {
                t.add(t.get(t.size() - 1) + K);
                helper(N, K, t);
            }
        }    
    }
    
    public int list2int(ArrayList<Integer> temp) {
        int result = 0;
        for (int i = 0; i < temp.size(); i++) {
            result *= 10;
            result += temp.get(i);
        }
        return result;
    }
}
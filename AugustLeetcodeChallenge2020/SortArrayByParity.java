class Solution {
    public int[] sortArrayByParity(int[] A) {
         for(int i = 0, even = 0; i < A.length; i++) {
             if (A[i] % 2 == 0) {
                 if (i > even){
                     int tmp = A[i];
                     A[i] = A[even];
                     A[even] = tmp;
                 }
                 even += 1;
             }
         }
        return A;
    }
}
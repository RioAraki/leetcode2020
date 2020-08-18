// smart solution

class Solution {
    public int maxProfit(int[] prices) {
        int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE;
        int release1 = 0, release2 = 0;
        for (int i : prices) {
            hold1 = Math.max(hold1, -i);
            release1 = Math.max(hold1+i,release1);
            hold2 = Math.max(hold2, release1-i);
            release2 = Math.max(release2, hold2+i);
            System.out.println("" +hold1 +" " + release1 +" " + hold2 +" " + release2);
        }
        return release2;
    }
}

// need to think about the dp solution
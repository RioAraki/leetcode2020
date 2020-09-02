class Solution {
    public boolean isPalindrome(String s) {
        // loop through all chars in string and filter out non-alphanumeric characters and to lower case
        StringBuilder sb = nonAlphanumericLowercaseConverter(s);
        return checkPalindrome(sb);
        
        // normal isPalindrome
    }
    
    // java lambda?
    public StringBuilder nonAlphanumericLowercaseConverter(String s) {
        StringBuilder nonAlphanumericLowercase = new StringBuilder();
        for (char ch: s.toCharArray()) {
            if (Character.isLetterOrDigit(ch)) {
                nonAlphanumericLowercase.append(Character.toLowerCase(ch));
            }
        }
        return nonAlphanumericLowercase;
    }
    
    public boolean checkPalindrome(StringBuilder s) {
        int halfSize = (int) Math.floor(s.length() / 2);
        for (int i = 0; i < halfSize; i++) {
            if (s.charAt(i) != s.charAt(s.length()-1-i)) {
                return false;
            }
        }
        return true;
    }
}
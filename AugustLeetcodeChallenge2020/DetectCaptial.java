
// Given a word, you need to judge whether the usage of capitals in it is right or not.

// We define the usage of capitals in a word to be right when one of the following cases holds:

// All letters in this word are capitals, like "USA".
// All letters in this word are not capitals, like "leetcode".
// Only the first letter in this word is capital, like "Google".
// Otherwise, we define that this word doesn't use capitals in a right way.



class Solution {
    public boolean detectCapitalUse(String word) {
        if (word.length() <= 1) {
            return true;
        } else {
            String noFirstChar = word.substring(1,word.length());
            if (noFirstChar == noFirstChar.toLowerCase()) {
                return true;
            } else {
                if (word == word.toUpperCase()) {
                    return true;
                } else {
                    return false;
                }
            }
        }
    }
}
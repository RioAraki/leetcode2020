class Solution {
    
    Set<Character> vowels = new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I','O', 'U'));
    
    public String toGoatLatin(String S) {
        // split sentence to words, deal with each word
        StringBuilder result = new StringBuilder();
        String[] wordList = S.split(" ");
        for (int i = 0; i < wordList.length; i++) {
            StringBuilder curWord = wordLatin(wordList[i], i + 1);
            result.append(curWord);
            if (i < wordList.length - 1) {
                result.append(" ");
            }
        }
        return result.toString();
    }
    
    public StringBuilder wordLatin(String S, int idx) {
        StringBuilder goatWord = new StringBuilder();
        if (vowels.contains(S.charAt(0))) {
            goatWord.append(S);
        } else {
            goatWord.append(S.substring(1));
            goatWord.append(S.charAt(0));
        }
        goatWord.append("ma");
        goatWord.append(new String(new char[idx]).replace("\0", "a"));
        return goatWord;
    }
}

public String toGoatLatin(String S) {
    Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
    String res = "";
    int i = 0, j = 0;
    for (String w : S.split("\\s")) {
        res += ' ' + (vowels.contains(w.charAt(0)) ? w : w.substring(1) + w.charAt(0)) + "ma";
        for (j = 0, ++i; j < i; ++j) {
            res += "a";
        }
    };
    return res.substring(1);
}
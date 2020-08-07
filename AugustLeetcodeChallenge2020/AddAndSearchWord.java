// generate a-z combination if meet . -> TLE


class WordDictionary {
    HashSet<String> wordSet;
    /** Initialize your data structure here. */
    public WordDictionary() {
        wordSet = new HashSet<>();
    }
    
    /** Adds a word into the data structure. */
    public void addWord(String word) {
        wordSet.add(word);
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        if (word.length() == 0) {
            return true;
        }
        ArrayList<StringBuilder> wordList = possibleWords(word);
        
        for (StringBuilder w: wordList) {
            if (wordSet.contains(w.toString())) {
                return true;
            }
        }
        return false;
    }
    
    public ArrayList<StringBuilder> possibleWords(String word) {
        ArrayList<StringBuilder> wordList = new ArrayList<StringBuilder>();
        for (char ch: word.toCharArray()) {
            if (wordList.size() == 0) {
                if (ch == '.') {
                    for (char alphabet = 'a'; alphabet <= 'z'; alphabet++) {
                        StringBuilder sb = new StringBuilder();
                        sb.append(alphabet);
                        wordList.add(sb);
                        
                    }
                } else {
                    StringBuilder sb = new StringBuilder();
                    sb.append(ch);
                    wordList.add(sb);
                }
            } else {
                if (ch == '.') {
                    ArrayList<StringBuilder> newWordList = new ArrayList<StringBuilder>();
                    for (StringBuilder w: wordList) {
                        for (char alphabet = 'a'; alphabet <= 'z'; alphabet++) {
                            StringBuilder loop = new StringBuilder(w.toString());
                            loop.append(alphabet);
                            newWordList.add(loop);
                        }
                    }
                    wordList = newWordList;
                } else {
                    for (StringBuilder w: wordList) {
                        w.append(ch); 
                    }
                }
                
            }
        }
        return wordList;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

// need to use trie, understand trie!
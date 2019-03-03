class Solution {
public:
    
    void reverseWord(string &s, int i, int j){
        while (i<j){
            char t = s[i];
            s[i++] = s[j];
            s[j--] = t;
        }
    }
    
    string reverseWords(string &s) {
        int i = 0; // real length
        int j = 0; // expected length (trim blanks)
        int l = 0; // l ?
        int len = s.length();
        int wordcount = 0;
        
        while (true) {
            while (i < len && s[i] == ' ') i++; // do nothing to all spaces in orginal string
            if (i == len) break;
            if (wordcount) s[j++]=' '; // manually create one ' ' after word exists
            
            l = j; // beginning of a word
            while(i < len && s[i] != ' ') { // s[i] is a char
                s[j] = s[i]; // j always < i
                j++;
                i++;
            }
            // the word ends at some point
            reverseWord(s, l, j-1);
            wordcount++;
            
        }
        
        s.resize(j);
        reverseWord(s,0,j-1);
        
        return s;
    }
};
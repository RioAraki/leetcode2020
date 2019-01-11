#include <iostream>
#include <string>

using namespace std;

int chr2int(char x) 
{
  switch(x){
    case 'I': return 1;
    case 'V': return 5;
    case 'X': return 10;
    case 'L': return 50;
    case 'C': return 100;
    case 'D': return 500;
    case 'M': return 1000;
  }
  
}

int solution(string roman) {
  int out = 0;
  for (int i = 0; i < roman.size(); ++i) {
    if (i < roman.size()-1) {
      if (chr2int(roman[i]) < chr2int(roman[i+1])) {
        out -= chr2int(roman[i]);
      } else {
        out += chr2int(roman[i]);
      }
    } else {
      out += chr2int(roman[i]);
    }
    
  }
  return out;
}
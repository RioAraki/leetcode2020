#include <string>
#include <iostream>

std::string strWithout3a3b(int A, int B) {
  std::string ret = "";
  // BASE CASE
  while (A + B > 2) {
    if (A > B) {
      ret.append("aab");
      A -= 2;
      B -= 1;
    }
    else if (B > A) {
      ret.append("abb");
      A -= 1;
      B -= 2;
    }
    else if (A == B) {
      ret.append("ab");
      A -= 1;
      B -= 1;
    }
  }

  if (A > 0) {
    ret.append(std::string(A, 'a'));

  }
  if (B > 0) {
    ret.insert(0, std::string(B, 'b'));

  }
  return ret;
}

int main() {
  std::string out = strWithout3a3b(10, 5);
  std::cout << out << std::endl;
  std::cin.get();
  return 0;
}
int root(int n) {
  int result = 0;
  while (n >= 10) {
    result += n % 10;
    n /= 10;
  }
  return result + n;
}


int digital_root(int n)
{
    int result;
    result = root(n);
    while (result >= 10){
      result = root(result);
    }
    return result;
    
}
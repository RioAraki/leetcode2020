std::string tickets(const std::vector<int> peopleInLine){
  std::map<int, int> keep;
  keep.emplace(25,0);
  keep.emplace(50,0);
  keep.emplace(100,0);
//   keep.insert(std::pair<int, int>(100,0));
  
  for (int people : peopleInLine) {
    if (people == 25) {
      keep[25] += 1;
    } else if (people == 50) {
      if (keep[25] == 0) {
        return "NO";
      } else{
        keep[25] -= 1;
        keep[50] += 1;
      }
    } else if (people == 100) {
      if (keep[50] > 0 && keep[25] > 0) {
        keep[25] -= 1;
        keep[50] -= 1;
        keep[100] += 1;
      } else if (keep[25] >= 3) {
        keep[25] -= 3;
        keep[100] += 1;
      } else {
        return "NO";
      }
    
    }
  }
  return "YES";
  
}
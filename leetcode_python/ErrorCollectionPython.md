# Error collection

A list of common syntax/ logical error I made when solving leetcode question by python. My goal is to achieve "one time accepted" for all easy/ medium level questions with python without any assist (like checking api). This requires the proficiency to python, think carefully about all possible corner cases and a quick mind to think about the best and accurate algorithms.

So far I could solve most of questions with 3-10 attempts, and a lot of times my answer causes TLE (time limit exceeded) which indicates my answer is correct but inefficiency. In order to have a better understand about my performance and where I could improve most, here I want to create this collection recording all different failing types and I have met and how often do I face to them.

## Error table

| Failure types   | nums    | Met in  |
| :-------------: |:-------:| :-----: |
| index error     | 7       | 830, 11, 64, 842, 72, 97, 849 |
| variable misuse | 1       | 830 |
| corner case     | 4       | 830, 63, 841, 845 |
| logic error     | 8       | 831, 11, 16, 63, 840, 72, 849, 853, 854 |
| TLE             | 5	    | 11, 97, 845, 29, 848      |
| indent error    | 2       | 63    |
| misunderstanding| 3       | 841, 842, 845     |
| type error      | 1       | 842     |
| syntax error    | 1       | 841     |
## Failure types detail

1. Index error: all error caused by miscalculating index (use list[len(list)] as the last element, wrong use of range(a,b) to get element, ...
2. variable misuse: use variable a when we actually need to use variable best
3. corner case: forgot to consider corner case like when input is empty/ 0/ invalid/ initial case for a recursion/ ...
4. logic error: wrong logic
5. TLE: time limit exceeded, answer may be right but too inefficient
6. Indent error: wrong indent in python
## Weekly Contest 78

### Q1 [811. Subdomain Visit Count](https://leetcode.com/contest/weekly-contest-78/problems/subdomain-visit-count/)
My answer - Python:
```
def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        output = []
        for domains in cpdomains:
            num, domain = domains.split(' ')[0], domains.split(' ')[1] # mistake 1:typo domain <-> domains
            subdomain_list = domain.split('.')
            if len(subdomain_list) == 3:
                subdomain1 = subdomain_list[2]
                subdomain2 = subdomain_list[1] + '.' + subdomain1
                subdomain3 = subdomain_list[0] + '.' + subdomain2
            else:
                subdomain1 = subdomain_list[1]
                subdomain2 = subdomain_list[0] + '.' + subdomain1
            if subdomain1 not in dict:
                dict[subdomain1] = int(num)
            else:
                dict[subdomain1] += int(num)  # mistake 5: messed up between string concatenation and number addition
            if subdomain2 not in dict:
                dict[subdomain2] = int(num)
            else:
                dict[subdomain2] += int(num)
            if len(subdomain_list) == 3: # mistake 4: wrong about the check way    if subdomain3:
                if subdomain3 not in dict:
                    dict[subdomain3] = int(num)
                else:
                    dict[subdomain3] += int(num)
        
        for key in dict: # mistake 2: about loop through a dict correctly
            string = "{} {}".format(str(dict[key]), key) # mistake 3, wrong order
            output.append(string)
        return output
```
Time used: 1hr

Better Answer:
```
    def subdomainVisits(self, cpdomains):
        domains = {}
        for st in cpdomains:
            snum, address = st.split(' ')
            num = int(snum)
            addr = address.split('.')
            n = len(addr)
            for i in range(n):
                domain = ".".join(addr[i:])  # key difference, one line to join all subdomain in all cases
                if domain in domains:
                    domains[domain]+=num
                else:
                    domains[domain]=num
        answer = []
        for domain in domains:
            answer.append(str(domains[domain])+" "+domain)
        return answer
```
Lesson learnd: `'string'.join(list)` would concatenate the list with 'string'

### Q2 [809. Expressive Words](https://leetcode.com/contest/weekly-contest-78/problems/expressive-words/)

My Answer - Python:
use regex on each candidate to judge if its valid
```
import re

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # (h|h{3,})(e|e{3,})(lll|l{5,})(o|o{3,})$
        regex = ''
        result = 0
        for word in words:
            word_list = list(word)
            repeat = 1
            for i in range (len(word_list)):
                if i == len(word_list) - 1:
                    if word_list[i] != word_list[i-1]:
                        repeat = 1
                    regex += '({}|{}{{{},}})'.format(word_list[i]*repeat, word_list[i], max(3, repeat)) // error one: misunderstand the meaning of group 
                else:       
                    
                    if word_list[i] != word_list[i+1]:
                        regex += '({}|{}{{{},}})'.format(word_list[i]*repeat, word_list[i], max(3, repeat))
                        repeat = 1
                    elif word_list[i] == word_list[i+1]:
                        repeat += 1
            regex += '$'
            if re.match(regex, S):
                result += 1
            regex = ''
        return result // error two: tle
```
Time used: 1.5 hrs

Time Limit Exceeded, need to think about the mechanic of regex and the runtime/ efficiency of it.

Better Answer
```
def expressiveWords(self, S, words):
        def signature(word): # 把word给简化成一个列表，第一位是（不重复的）字母，第二位是字母出现的次数
            if word=="":
                return []
            n = len(word)
            answer = [word[0],1]
            for i in range(1,n):
                if word[i]==word[i-1]: # 相同字母连续出现的情况
                    answer[-1]+=1
                else:
                    answer.extend([word[i],1])
            return answer
        
        sgn = signature(S)    
                
        def stretched(word):
            sgn2 = signature(word) # 做同样操作
            if len(sgn)!=len(sgn2): # 长度不同说明有字不一样，肯定错
                return False
            n = len(sgn)
            for i in range(n):
                if i%2==0:
                    if sgn[i]!=sgn2[i]: # 字不同肯定错
                        return False
                if i%2==1: 
                    if sgn[i]<=2 and sgn2[i]!=sgn[i]: 
                        return False
                    elif sgn2[i]>sgn[i]:
                        return False
            return True # 排除所有错误情况后得到的正确答案

            
        return sum([1 for word in words if stretched(word)])
        # 1 行的 syntax sugar
```
Lesson learnd: 
    - the way he interpret this question is much better than i do, espcially the data structure (list with char and num appeared) and the idea to cut all wrong options to get the correct answer.
    - syntax sugar: `sum([1 for word in words if stretched(word)])`
    - regex could be slow to parse (so far i cant tell precisely the reason, its relate to the implementation and i dont want to dig too deep right now), maybe try to avoid in code competition

### Q3

### Q4
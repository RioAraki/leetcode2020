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

### Q2

### Q3

### Q4
# See the pattern of english numbering like thousand, million, billion, etc.
# corner case: 0, 1, 100, 1000, 1001, 1000001

class Solution:
    def numberToWords(self, num: int) -> str:
        n = len(str(num))
        # xxx(billion) xxx(million) xxx(thousand)  x(hundred) xx
        bitDct = {0:"", 1:" Thousand", 2:" Million", 3: " Billion"}
        
        # the input char is a reverse string with length <= 3
        def hundred2Words(string):
            
            if string == "000": return ""
            n = len(string)
            dct1 = {"1": " One","2": " Two","3": " Three","4": " Four","5": " Five","6": " Six","7": " Seven","8": " Eight","9": " Nine","0": ""}
            dct2 = {"2": " Twenty","3": " Thirty","4": " Forty","5": " Fifty","6": " Sixty","7": " Seventy","8": " Eighty","9": " Ninety","0": ""}
            dct3 = {"1": " Eleven", "2": " Twelve", "3":" Thirteen", "4": " Fourteen", "5": " Fifteen", "6": " Sixteen", "7": " Seventeen", "8":" Eighteen", "9": " Nineteen", "0": " Ten"}
            # reverse string with length <= 2
            def ten2Words(string, dct1, dct2, dct3):
                n = len(string)
                if int(string) == 0:
                    return ""
                if n == 1:
                    return dct1[string[0]]
                elif n ==2:
                    if string[1] == "1":
                        return dct3[string[0]]
                    else:
                        ret = dct2[string[1]] + dct1[string[0]]
                        return ret
            if n <= 2:
                return ten2Words(string, dct1, dct2, dct3)
            else:
                
                if string[2] != "0":
                    return dct1[string[2]] + " Hundred" + ten2Words(string[:2], dct1, dct2, dct3)
                else:
                    
                    return ten2Words(string[:2], dct1, dct2, dct3)
        
        if num == 0:
            return "Zero"
        
        reverse = str(num)[::-1]
        cnt = 3
        bit = 0
        ret = ""
        while cnt <= n:
            part = hundred2Words(reverse[cnt-3:cnt])
            ret = part + bitDct[bit] + ret if part != "" else "" + ret
            cnt += 3
            bit += 1
            
        if n%3 != 0:
            part = hundred2Words(reverse[cnt-3:n])
            ret = part + bitDct[bit] + ret
            
        return ret.strip()
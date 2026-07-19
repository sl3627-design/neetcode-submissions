class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""

        len_gcd = math.gcd(len(str1), len(str2))

        if str2[:len_gcd]*(len(str1)//len_gcd) == str1:
            return str1[:len_gcd]
        
        return res


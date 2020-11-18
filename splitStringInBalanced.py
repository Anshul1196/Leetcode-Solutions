class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal=0
        ans=0
        for n in range(0,len(s)):            
            if (s[n] == "L"):
                bal= bal+1
            else:
                bal= bal-1
            if(bal == 0):
                ans= ans+1
        return ans
            

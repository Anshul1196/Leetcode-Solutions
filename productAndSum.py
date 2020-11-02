class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        while(n > 0):
            rem= n%10            
            sum = sum+rem
            product = product * rem
            n = int(n/10)       
        result= product- sum
        return result

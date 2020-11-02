class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evendigits=0
        for i in nums:
            count =0
            while(i != 0):
                i = int(i/10)
                count = count + 1                
            if(count%2==0):
                evendigits= evendigits + 1
                print("Even digits")
            else:
                print("Odd digits")
        print(evendigits)
        return evendigits

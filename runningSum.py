class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        temp=0
        for i in nums:          
            temp = temp + i
            arr.append(temp)
        print(arr)
        return arr

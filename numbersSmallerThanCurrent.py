class Solution:
    def smallerNumbersThanCurrent(self, nums):        
        ans=[]
        count=0
        for i in nums:
            for j in range(len(nums)):
               if (nums[j]-i)<0:
                   count+=1
            ans.append(count)
            print(ans)
            count=0
        return ans         
            

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans_list=[]
        lis=dict()
        for i in range(0, len(nums)-1,2):           
            lis["freq"]=nums[i]
            lis["val"]= nums[i+1]
            for k in range((lis["freq"])):
                ans_list.append(lis["val"])          
        return ans_list

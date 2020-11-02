class Solution:
    def replaceElements(self, arr):
        l= len(arr)
        ans=[]
        for i in range(l-1):
            ans.append(max(arr[i+1:]))
        ans.append(-1)
        return ans

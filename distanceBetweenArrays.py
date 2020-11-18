class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        flag=0
        for i in range(0,len(arr1)): 
            flag=1
            for j in range(0,len(arr2)):
                if (abs(arr1[i]-arr2[j]) <= d):
                    flag=0;
                    break;
            if flag:
                count= count+1
        return count
        

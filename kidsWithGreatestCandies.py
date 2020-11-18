class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies=max(candies)
        res_list=list()
        for i in range(0,len(candies)):
            if (candies[i]<max_candies):
                to_add= max_candies-candies[i] 
                if (to_add > extraCandies):
                     res_list.append(False)
                else:   
                    check_candies= to_add + extraCandies
                    res_list.append(True)
            else:
                res_list.append(True)
        return res_list
                    

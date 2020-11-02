class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans_list = list()
        s_list = list(s)
        for i in range(0, len(indices)):
            ind = indices.index(i)
            ans_list.append(s_list[ind])
            #print(ans_list)
            str1 = "".join(ans_list)
            #print("\"%s\""% str1 )
        return str1
            

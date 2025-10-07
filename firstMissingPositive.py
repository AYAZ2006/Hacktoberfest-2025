class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashs={}
        for elem in nums:
            if elem>0:
                hashs[elem]=1
        res=1
        for _ in range(len(hashs)):
            if res in hashs:
                res+=1
            else:
                return res
        return res


        

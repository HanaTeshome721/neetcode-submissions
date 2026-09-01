class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nm=Counter(nums)
        res=[]
        for n,cn in nm.items():
            if cn > len(nums)//3:
                res.append(n)
        return res                
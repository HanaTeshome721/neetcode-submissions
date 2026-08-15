class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[1]*len(nums)

        pm=1
        for i in range(len(nums)):
            res[i]=pm
            pm*=nums[i]
        pf=1    
        for i in range(len(nums)-1,-1,-1):
            res[i]*=pf
            pf*=nums[i]
        return res       
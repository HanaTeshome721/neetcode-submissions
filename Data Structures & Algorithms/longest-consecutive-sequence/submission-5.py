class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            # nus=set(nums)
            # res=0
            # for i in range(len(nums)):
            #     cnt=0
            #     cur=nums[i]
            #     while cur in nus:
            #       cnt+=1
            #       cur+=1
            #     res=max(cnt,res)
            # return res      
            if not nums:
                return 0
            nums.sort()
            long=1
            res=1
            i=1
            while i <len(nums):
                
                if nums[i]==nums[i-1]:
                    i+=1
                    continue
                if nums[i]==nums[i-1]+1:
                    res+=1
                    
                else:
                    
                    long=max(res,long)
                    res=1
                i+=1    
            long=max(res,long)    
                    
            return long        
                        
                
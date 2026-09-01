class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       res=cur=0 
       pref={0:1}
       for i in range(len(nums)):
            cur+=nums[i]
            diff=cur-k
            res+=pref.get(diff,0) 
            pref[cur]=1 + pref.get(cur,0)
       return res    
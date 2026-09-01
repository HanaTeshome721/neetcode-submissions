class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
   #   st=set(nums)
     for n in range(1,len(nums)+2):
         if n not in nums:
            return n
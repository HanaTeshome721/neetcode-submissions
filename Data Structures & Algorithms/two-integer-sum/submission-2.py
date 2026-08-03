class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i,n in enumerate(nums):
            if n not in d:
              d[n]=i
             
            diff=target-n
            if diff in d and d[diff]!=i:
                return [d[diff],i]   
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)

        arr=[]
        for num,cnt in count.items():
           arr.append([cnt,num]) 
        arr.sort()
        ans=[]
        while k>0:
            ans.append(arr.pop()[1])
            k-=1
        return ans    

           
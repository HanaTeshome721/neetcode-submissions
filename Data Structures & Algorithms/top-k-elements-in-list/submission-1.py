class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)

        # arr=[]
        # for num,cnt in count.items():
        #    arr.append([cnt,num]) 
        # arr.sort()
        # ans=[]
        # while k>0:
        #     ans.append(arr.pop()[1])
        #     k-=1
        # return ans   

        heap=[]
        for n,frq in count.items():
            heapq.heappush(heap,(frq,n))
            if len(heap)>k:
                heapq.heappop(heap)
        result =[]
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result    


           
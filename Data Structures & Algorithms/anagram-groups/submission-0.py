class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for i,w in enumerate(strs):
            # print(sorted(w))
            w= ''.join(sorted(w))
            if w in ans:
                ans[w].append(i)
            else:
                ans[w]=[i]
                
        final=[]
        for k,v in ans.items():
            val=[]
            for i in v:
                val.append(strs[i])
            final.append(val)    
        return final                       

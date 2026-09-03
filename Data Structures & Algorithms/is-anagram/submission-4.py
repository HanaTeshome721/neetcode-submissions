class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # st=Counter(s)
        # tt=Counter(t)
        # if len(st)!=len(tt):
        #     return False
        # return st==tt
        # for c in tt:
        #     if st[c]!=tt[c]:
        #         return False
        # return True 
        s=list(s)
        t=list(t)       
        s.sort()
        t.sort()
        if len(s)!=len(t):
            return False
        u=len(s)    
        for i in range(u):
            if s[i]!= t[i]:
                return False
        return True        

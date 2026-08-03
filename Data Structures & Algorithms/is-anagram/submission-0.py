class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st=Counter(s)
        tt=Counter(t)
        if len(st)!=len(tt):
            return False
        for c in tt:
            if st[c]!=tt[c]:
                return False
        return True        
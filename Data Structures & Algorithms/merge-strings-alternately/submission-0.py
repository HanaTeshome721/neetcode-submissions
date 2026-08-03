class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=0
        r=0
        new=''
        n=len(word1)
        m=len(word2)
        while l<n and r<m:
            new+= (word1[l] + word2[r])
            l+=1
            r+=1
        if l<n:
            new+=word1[l:]
        if r<m:
            new+=word2[r:]
        return new    

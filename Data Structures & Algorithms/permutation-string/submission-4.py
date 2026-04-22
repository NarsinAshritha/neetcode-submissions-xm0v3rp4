class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
     l = 0
     hmap={}
     char=[]
     for i in s1:
        hmap[i]= hmap.get(i,0)+1     

     for r in range(len(s2)):
        if s2[r] in hmap:
            l=r
            char=s2[l:l+len(s1)]
            if sorted(s1)==sorted(char):
                return True
            else:
                continue
     return False
         
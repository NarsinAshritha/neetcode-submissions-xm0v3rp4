class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
     from collections import Counter
     l = 0
     hmap=Counter(s1)
     char=[]
     target=sorted(s1)
        

     for r in range(len(s2)):
        if s2[r] in hmap:
            l=r
            char=s2[l:l+len(s1)]
            if target==sorted(char):
                return True
            else:
                continue
     return False
         
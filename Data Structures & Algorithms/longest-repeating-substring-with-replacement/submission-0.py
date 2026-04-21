class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count={}
        maxlen=0
        ans=0

        for r in range(len(s)):
            count[s[r]]= count.get(s[r],0)+1
            maxlen= max(maxlen,count[s[r]])

            while (r-l+1) - maxlen > k:    #window - max freq <=k  
                  count[s[l]]-=1
                  l+=1
            ans = max(ans, r-l+1)
        return ans
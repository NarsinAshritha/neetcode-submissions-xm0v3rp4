class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     s_dict=dict()
     t_dict=dict()

     for char in s:
        if char not in s_dict:
            s_dict[char]=1
        else:
            s_dict[char]+=1   

     for j in t:
        if j not in t_dict:
            t_dict[j]=1
        else:
            t_dict[j]+=1  
    
    # sort_s_dict = dict(sorted(s_dict.items()))
    # sort_t_dict = dict(sorted(t_dict.items()))

     return s_dict == t_dict
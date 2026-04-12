class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i,str in enumerate(strs):
            sstr = "".join(sorted(str))
            if sstr in hm.keys():
                hm[sstr].append(str)
            else:
                hm[sstr]=[str]
        return list(hm.values())

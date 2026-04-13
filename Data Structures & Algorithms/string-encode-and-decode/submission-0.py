class Solution:

    def encode(self, strs: List[str]) -> str:
        enstr=""
        for i in strs:
            enstr += str(len(i)) +"#" + i
        return enstr

    def decode(self, s: str) -> List[str]:
        decstr = []
        i = 0

        while i < len(s):
            # Step 1: find length
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Step 2: extract string
            word = s[j+1 : j+1+length]
            decstr.append(word)

            # Step 3: move pointer
            i = j + 1 + length

        return decstr
                

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hSet = []
        for s in strs:
            hashA = [0]*26
            for i in range(len(s)):
                hashA[ord(s[i])-ord('a')] +=1
            hSet.append(hashA)
        out = []
        seen = set()
        seenIndex = set()
        for i in range(len(hSet)):
            if strs[i] in seen and i in seenIndex: continue
            temp = []
            temp.append(strs[i])
            seen.add(strs[i])
            seenIndex.add(i)
            for j in range(i+1,len(hSet)):
                if strs[j] in seen and j in seenIndex: continue
                if hSet[i] == hSet[j]:
                    temp.append(strs[j])
                    seen.add(strs[j])
                    seenIndex.add(j)
            out.append(temp)
        return out



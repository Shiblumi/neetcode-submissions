from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count1 = Counter(s)
        # count2 = Counter(t)

        # return count1 == count2

        count1 = {}
        count2 = {}

        for c in s:
            if c in count1:
                count1[c] += 1
            else:
                count1[c] = 1
        for c in t:
            if c in count2:
                count2[c] += 1
            else:
                count2[c] = 1
        
        return count1 == count2
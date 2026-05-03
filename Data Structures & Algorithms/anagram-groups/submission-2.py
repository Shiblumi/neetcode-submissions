from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        done = set()
        ans = []

        for i1, w1 in enumerate(strs):
            if i1 in done:
                continue
            sub_list = [w1]
            done.add(i1)

            for i2, w2 in enumerate(strs):
                if i2 in done:
                    continue
                if Counter(w1) == Counter(w2):
                    sub_list.append(w2)
                    done.add(i2)
            
            ans.append(sub_list)
        
        return ans

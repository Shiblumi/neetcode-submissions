from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Create a list of lists len(k).
        # Use the idx to represent the # of times a number occurs.
        # Each elem is a list because multiple numbers can occur the same # of times.
        # len(nums) + 1 because we are not using zero index.
        top_k = [[] for _ in range(len(nums) + 1)]
        ans = []

        # idx == number of times a number occurs.
        for key, val in count.items():
            top_k[val].append(key)
        
        # Go in reverse since higher idx will have greatest occurrences.
        for curr in top_k[::-1]:
            # Break when we have k elems in our ans.
            if len(ans) >= k:
                break
            # Use extend() since we don't want to append a list to ans, but its elems.
            ans.extend(curr)

        return ans
        
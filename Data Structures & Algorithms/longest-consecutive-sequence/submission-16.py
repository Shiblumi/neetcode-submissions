class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_seq = 0
        
        for n in nums:
            # Only start counting if n is the start of a sequence 
            if n - 1 not in seen:
                # curr begins at an n that is the start of a sequence
                curr = n
                count = 0

                # Keep incrementing curr until it no longer exists in the set
                while curr in seen:
                    count += 1
                    curr += 1
                max_seq = max(max_seq, count)

        return max_seq
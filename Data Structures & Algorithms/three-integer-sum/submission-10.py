class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # Sorting is key to use two pointers to check sum
        nums.sort()

        for i, v in enumerate(nums):
            # Guard clause to avoid considering dup values of v
            if i > 0 and v == nums[i-1]:
                continue
            # l starts one after i, r starts at end [i->, l->, ... , <-r]
            l, r = i+1, len(nums)-1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # Sum too high, push r to smaller num
                if s < 0:
                    l += 1
                # Sum too low, push l to bigger num
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # Shift l and r to consider remaining possibilities
                    l += 1
                    r -= 1
                    # Keep shifting l until it no longer points to a dup value (can also shift r, doesn't matter)
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ans
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ans

        # seen = set()
        # ans = []
        # nums.sort()

        # for i, n in enumerate(nums):
        #     if i == 0 or i == len(nums)-1:
        #         continue
        #     l = 0
        #     r = len(nums) - 1
        #     print(f'Considering {l}, {i}, {r}')
            
        #     while l < i and r > i:
        #         sum = nums[l] + nums[r] + n
        #         if sum > 0:
        #             r -= 1
        #         elif sum < 0:
        #             l += 1
        #         elif sum == 0:
        #             combination = (nums[l], nums[r], n)
        #             if combination in seen:
        #                 break
        #             ans.append([nums[l], nums[r], n])
        #             seen.add((nums[l], nums[r], n))
        #             break
        # return ans
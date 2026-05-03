class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = []
        postfix = []

        prod = 1
        for n in nums:
            prod *= n
            prefix.append(prod)

        prod = 1
        for n in nums[::-1]:
            prod *= n
            postfix.append(prod)
        postfix.reverse()

        print(f"prod_og: {nums}")
        print(f"prefix: {prefix}")
        print(f"postfix: {postfix}")

        for i, _ in enumerate(nums):
            if i == 0:
                ans.append(postfix[i+1])
            elif i == len(nums) - 1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1] * postfix[i+1])

        return ans
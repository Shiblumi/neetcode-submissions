class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Needcode solution is shorter & cleaner, but I understand this more.
        ans = []
        prefix = []
        postfix = []

        # Create prefix list
        prod = 1
        for n in nums:
            prod *= n
            prefix.append(prod)

        # Create postfix list then reverse produced list
        prod = 1
        for n in nums[::-1]:
            prod *= n
            postfix.append(prod)
        postfix.reverse()

        print(f"prod_og: {nums}")
        print(f"prefix: {prefix}")
        print(f"postfix: {postfix}")

        # For i in ans, multiply i-1 of prefix (left) and i+1 of postfix (right) 
        for i, _ in enumerate(nums):
            # If first element, there's no element i-1 so assume 1
            if i == 0:
                ans.append(postfix[i+1])
            # If last element, there's no element i+1 so assume 1
            elif i == len(nums) - 1:
                ans.append(prefix[i-1])
            # Multiply i-1 of prefix and i+1 of postfix
            else:
                ans.append(prefix[i-1] * postfix[i+1])

        return ans
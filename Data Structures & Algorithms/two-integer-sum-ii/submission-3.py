class Solution:
    # Key point: The numbers list is sorted
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Left pointer at start of numbers list, right pointer at end
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            # If sum is less than target, left pointer needs to point to a larger num
            if sum < target:
                left += 1
            # If sum is greater than target, right pointer needs to point to a smaller num
            elif sum > target:
                right -= 1
            elif sum == target:
                return [left+1, right+1]
        
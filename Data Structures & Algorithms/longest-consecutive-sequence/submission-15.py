class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_seq = 0
        
        for n in nums:
            
            if n - 1 not in seen:
                curr = n
                count = 0
                while curr in seen:
                    count += 1
                    curr += 1
                max_seq = max(max_seq, count)
                count = 0

        return max_seq
        # if not nums:
        #     return 0

        # max_num = max(nums)
        # min_num = min(nums)
        # my_list = [False for _ in range(abs(min_num) + max_num + 1)]
        # max_seq = 0
        # print(my_list)
        # print('len', len(my_list))

        # for n in nums:
        #     idx = n + abs(min_num)
        #     print('idx', idx)
        #     my_list[idx] = True
        
        # print(my_list)
        # count = 0
        # for b in my_list:
        #     if b:
        #         count += 1
        #     else:
        #         max_seq = max(max_seq, count)
        #         count = 0
        # max_seq = max(max_seq, count)
        
        # return max_seq
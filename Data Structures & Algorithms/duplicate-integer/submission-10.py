class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        num_counter = {} #num, count

        for i, num in enumerate(nums):
            num_counter[num] = 1 + num_counter.get(num, 0)

        if all(value == 1 for value in num_counter.values()):
            return False
        else:
            return True
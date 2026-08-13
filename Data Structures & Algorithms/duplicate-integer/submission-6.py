class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = dict.fromkeys(nums,0)

        for value in nums:
            count[value] += 1

        return any(val != 1 for val in count.values())
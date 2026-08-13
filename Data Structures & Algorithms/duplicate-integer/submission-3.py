class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums)-1):
            num_1 = nums[i]
            num_2 = nums[i+1]

            if(num_1 == num_2):
                return True

        return False
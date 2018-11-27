class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m={}
        for i in range(len(nums)):
            if nums[i] in m:
                return [m[nums[i]],i]
            else:
                m[target-nums[i]] = i

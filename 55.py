class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pos = 0
        nlen = len(nums)
        fuel = 0
        while pos != fuel or nums[pos] != 0:
            if pos + nums[pos] > fuel:
                fuel = pos + nums[pos]
                if fuel >= nlen - 1:
                    return True
            pos += 1
        return False if pos != nlen - 1 else True

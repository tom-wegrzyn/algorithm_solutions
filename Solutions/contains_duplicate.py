class Solution:
    def containsDuplicateFirstIteration(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums:
            nums.sort()
            while len(nums) > 0:
                valueToFindDupe = nums.pop(0)
                if self.binarySearch(nums, valueToFindDupe):
                    return True
        return False

    @staticmethod
    def binarySearch(array, target):
        start, mid, end = 0, 0, len(array) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    @staticmethod
    def containsDuplicateSecondIteration(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers = set(nums)
        if len(numbers) != len(nums):
            return True
        return False
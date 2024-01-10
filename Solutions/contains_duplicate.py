class Solution:
    def contains_duplicate_first_iteration(self, nums: list[int]) -> bool:
        """
        Takes in a list of numbers and determines if the list contains a duplicate.

        Parameters
        ----------
        self : Instance
            The instance of the class to access helper methods
        nums : List[int]
            The list of numbers to find a duplicate in.

        Returns
        ----------
        bool
            True or false depending on if the list contains a duplicate.
        """
        if nums:
            nums.sort()
            while len(nums) > 0:
                valueToFindDupe = nums.pop(0)
                if self.binary_search(nums, valueToFindDupe):
                    return True
        return False

    @staticmethod
    def binary_search(array: [int], target: int) -> bool:
        """
        Takes in an array of numbers and searches for the target parameter in the array
        implementing the binary search method.

        Parameters
        ----------
        array : array[int]
            An array of numbers to search through
        target : int
            A number to find inside the array

        Returns
        ----------
        bool
            True or false depending on if the array contains the value.
        """
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
    def contains_duplicate_second_iteration(nums: list[int]) -> bool:
        """
        Takes in a list of numbers and determines if the list contains a duplicate.

        Parameters
        ----------
        nums : List[int]
            The list of numbers to find a duplicate in.

        Returns
        ----------
        bool
            True or false depending on if the list contains a duplicate.
        """
        numbers = set(nums)
        if len(numbers) != len(nums):
            return True
        return False

class Solution:
    @staticmethod
    def two_sum(nums: list[int], target: int) -> list[int]:
        """
        Takes in list of numbers and a target value and determines if two of the ints in the list can add
        up to the target.

        Parameters
        ----------
        nums : list[int]
            The list of values that can potentially add up to the target.
        target : int
            The target sum.

        Returns
        ----------
        list[int]
            A list containing the indexes of the integers that add up to the target.
        """
        if len(nums) <= 1:
            return []
        for x in range(0, len(nums) - 1):
            value = target - nums[x]
            for c in range(x + 1, len(nums)):
                if nums[c] == value:
                    return [x, c]
        return []


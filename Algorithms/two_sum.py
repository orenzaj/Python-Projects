# Given a list of numbers, find two numbers that add up to the target number.
import timeit

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}

        # Check if list is at least 2 numbers.
        if len(nums) > 1:
            # Enumerate the list to get value and index
            for i, num1 in enumerate(nums):
                # Get complement
                num2 = target - num1
                #print("nums[{}] = {}, num2 = {}, sum = {}".format(i, num1, num2, target))

                # Check the keys for complement of current number
                if num2 in dic:
                    return[nums.index(num2), i]
                # Store the value seen in dictionary
                dic[num1] = i
                print("dic = \t {}\n".format(dic))
            else:
                return "No two numbers add up to target."
        else:
            return "Not enough items in the list."


if __name__ == "__main__":
    nums = [1,2,3,4,7]
    target = 10
    sol = Solution()
    #print(timeit.timeit(Solution.twoSum(Solution, nums, target)))
    print(sol.twoSum(nums, target))

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Finds the indices of two numbers in `nums` that add up to `target`.

    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        A list of two indices, where `nums[i] + nums[j] == target`,
        or None if no such pair exists.

    Time complexity: O(n), where n is the length of `nums`.
    Space complexity: O(n) for the dictionary used to store numbers and indices.
    """

    num_map = {}

    for i, num in enumerate(nums):
        print("Current value of num:", num)
        complement = target - num
        print("Complement:", complement)

        if complement in num_map:
            print("Found pair:", [num_map[complement], i])
            return [num_map[complement], i]

        num_map[num] = i

    return None

# Test case
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print("Final result:", result)

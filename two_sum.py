def two_sum(nums: list[int], target: int) -> list[int]:
   """
   Finds the indices of two numbers in `nums` that add up to `target`.

   Args:
       nums: A list of integers.
       target: The target sum.

   Returns:
       A list of two indices, where `nums[i] + nums[j] == target`, or None if no such pair exists.
   """

   num_map = {}  # Use a dictionary for efficient lookups

   for i, num in enumerate(nums):
       complement = target - num
       if complement in num_map:
           return [num_map[complement], i]  # Return indices of the pair
       num_map[num] = i  # Store current number and its index

   return None  # No matching pair found

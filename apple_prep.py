"""
Two sum

"""
def two_sum(nums, target):
	"""
	return the inddices of the nums that sum to target"""
	nums_map = {}
	for i in range(len(nums)):
		key = nums[i]
		value = i 
		nums_map[key] = value

	for i in range(len(nums)):
		compliment = target - nums[i]
		if compliment in nums_map and nums_map[compliment] != i:
			return [i, nums_map[compliment]]
	return []


def three_sum(nums, target):
	"""
	Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

	for i in range(len(nums)):
		fix_i= nums[i]
		new_target = -fix_i
		two_sum_output = two_sum(nums[:i] + nums[i+1:], new_target)
		if two_sum_output:
			x = nums[i]
			y = two_sum_output[0]
			z = two_sum_output[1]
			return x,y,z
	return [] 

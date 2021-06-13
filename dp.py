def knapsack(weights, items_values, weight_capacity):
	"""
	we have an array of items, and a bunch of vals
	"""
	rows = len(weights) # we need a column of zeros
	columns = weight_capacity + 1

	table = [[0 for x in range(columns)] for y in range(rows)]

	# we want to continue to add one more item into the bag
	# iterate over items, then iterate over colums
	for i in range(rows):
		for curr_capacity in range(columns):

			#if the the item weighs more than the capacity at that column, 
			# then just look at the weight above, because we can't add the item to our bag. 
			if weights[i] > curr_capacity:
				table[i][curr_capacity] = table[i - 1][curr_capacity]

			#if the value of the item is less than the capacity we have to do the max calculation. 
			else:
				leftover_weights = curr_capacity - weights[i]
				best_value_with_leftover_weights = table[i - 1][leftover_weights]
				best_value_with_new_item = items_values[i] + best_value_with_leftover_weights
				
				best_value_without_new_item = table[i - 1][curr_capacity] 
				table[i][curr_capacity] = max(best_value_with_new_item, best_value_without_new_item)
	return table





print("KNAPSACK")
vals = [1,4,5,7]
weights = [1,3,4,5]
capacity = 5
print(knapsack(weights, vals, capacity))


"""
Permutations - generate all the 
Combinations— all the combinations binary array [0,1[ length k 
Subsets— if I give you 1,2,3 create all subsets

Solve with recursion. 
"""
#With permutations we care about the order of the elements, THINK LOCKER COMBO

def swqp(i, j, input_lst):
	# print("input list be/ore: ", input_lst)
	i_value = input_lst[i]
	j_value = input_lst[j]
	input_lst[i] = j_value
	input_lst[j] = i_value
	# print("input_lst after: ", input_lst)
	return input_lst

def permuations(input_lst, curr_index):
	print("curr_index: ", curr_index)
	if curr_index == len(input_lst) -1:
		print(input_lst) 
		return 
	for i in range(curr_index, len(input_lst)):
		# print("i: ", i, "   curr index: ", curr_index)
		input_lst = swqp(i, curr_index, input_lst)
		permuations(input_lst, curr_index+1)

		#backtracking to top of tree
		input_lst = swqp(curr_index, i, input_lst) 

lst = ['A', 'B', 'C']
permuations(lst, curr_index=0)


# def get_coin_change(amount, coins):
# 	output = 100000
# 	if amount==0 or not coins: 
# 		return 
# 	if amount < 0:
# 		return float('inf')
# 	else:
# 		return min(get_coin_change(amount-coins[0], coins), get_coin_change(amount, coins[1:]))

# out = get_coin_change(11, [1,2,5])
# print(out)

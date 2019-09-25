from collections import Counter
def min_window(s, t):
	"""
	Input: S = "ADOBECODEBANC", T = "ABC"
	Output: "BANC"

	"""
	if not t or not s:
		return ""

	#Dictionary to keep a count of all unique characters in t.
	dict_t = Counter(t)

	# Number of unique characters in t, which needs to be present in the desired window.
	required = len(dict_t)

	#left pointer, right, pointer initialization
	left = 0
	right = 0

	# Now, we need a way to keep track of if we have a successful window or not.
	# we will use formed to do this. 
	formed = 0

	current_window = {}

	output = float("inf"), None, None

	#Now we will begin the sliding window approach. 
	while right < len(s):
		print(right)
		character = s[right]
		print(character)
		if character in current_window:
			current_window[character] += 1
		else:
			current_window[character] = 1



		if character in dict_t and current_window[character] == dict_t[character]:
			formed += 1


		# IF WE HAVE A WINDOW THAT WORKS
		while (left <= right and formed == required):
			character = s[left]

			#store this current solution if it is better than the old solution
			if right - left + 1 < output[0]:
				length = right - left + 1
				left_index = left 
				right_index = right
				output = (length, left_index, right_index)


			#now we see if we can contract the window. We move the left pointer up by one.
			current_window[character] -= 1
			if character in dict_t and current_window[character] < dict_t[character]:
				formed -= 1

			left += 1 # look for a new window.

		#increment right once we have contracted current window as much as possible. 
		right += 1

	if output[0] == float("inf"):
		return ""
	else:
		solution = s[output[1]:output[2] + 1] #remember indexing in python isn't inclusive on the right side. 
		return solution

S = "ADOBECODEBANC"
T = "ABC"
solution = min_window(S, T)
print(solution)

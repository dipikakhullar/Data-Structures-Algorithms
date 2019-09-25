def flatten(nested_list):
	output = []
	for element in nested_list:
		if type(element) == int:
			output.append(element)
		else:
			output += flatten(element)
	return output


example = [1,[2,[3,4,5,6],[7,8]]]

output = flatten(example)
print(output)


def rollTheString(s, roll):
    i = 0
    tmp = ''
    while i < len(s):
        if ( i < len(roll)):
        	ch_offset = roll[i]  
        else:
        	0
        tmp += (chr(ord(s[i]) + ch_offset))
        i += 1
    return tmp

newString = rollTheString("abz", [3, 3, 3])
print (newString)
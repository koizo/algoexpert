"""
https://www.algoexpert.io/questions/validate-subsequence
"""
def isValidSubsequence(array, sequence):
    # Write your code here.
    sub_array = array
	num_elemments = 0
	for sequence_element in sequence:
		for i in range(len(sub_array)):
			if sub_array[i] == sequence_element:
				num_elemments+=1
				sub_array=sub_array[i+1:]
				break
	return len(sequence)==num_elemments
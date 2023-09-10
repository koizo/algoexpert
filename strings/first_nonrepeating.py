"""
https://www.algoexpert.io/questions/first-non-repeating-character
"""
def firstNonRepeatingCharacter(string):
    # Write your code here.
	index = 0
	hashmap = {}
	while index < len(string):
		#print(string[index])
		if string[index] in hashmap:
			hashmap[string[index]]['count']=hashmap[string[index]]['count']+1
		else:
			hashmap[string[index]] = {'f':index,'count':1}
		index = index + 1
	#print(hashmap)
	index = 0
	for i in hashmap:
		if hashmap[i]['count']==1:
			return hashmap[i]['f']
		index = index + 1
		
	
    return -1
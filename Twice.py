import sys
with open('words.txt', 'r') as file:
    words = file.readlines()
words_hash = {}

def pre_process_dictionary():
	for word in words:
		word = word.rstrip("\n")
		sorted_word = "".join(sorted(word))
		words_list = words_hash.get(sorted_word)
		if type(words_list) == list:
			words_hash[sorted_word].append(word)
		else:
			words_hash[sorted_word] = [word]

  
def get_combinations(input):
	input = ''.join(sorted(input))
	output = []
	def helper(input, prefix):
		if not len(input):
			return None
		if prefix not in output: 
		    output.append(prefix)
		for letter in input:
			next_perm = ''.join(sorted(prefix + letter))
			if next_perm not in output:
			    output.append(next_perm)
		helper(input[1:], prefix + input[0])
	for i in range(1, len(input)):
	    helper(input[i:], input[i-1])
	return output

def solve():
	if len(sys.argv) < 2 or not sys.argv[1]:
		print "enter a word"
		return
	input_word = sys.argv[1]
	pre_process_dictionary()
	toPrint = []
	for combo in get_combinations(input_word):
		if words_hash.get(combo): 
			for elem in words_hash[combo]:
				if not elem == input_word:
				    toPrint.append(elem)
	toPrint.sort(key = lambda s: len(s))
	for i in range(len(toPrint)):
	    print toPrint[i]
solve()
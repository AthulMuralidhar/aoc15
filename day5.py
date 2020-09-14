	# FUNC 1
	# break the word into two pairs of alphabets
	# check for each pair if it is repeating

	# FUNC 2
	# break the word into alphabets
	# check for triads with first alphabet = last alphabet in
	# the triad

	# if word passed both func1 and func 2 add one to nice
	# counter
	# else add one to naughty counter


def nice_discriminator(word, nice_counter, naughty_counter):
	if pair_checker(word) and triad_checker(word):
		nice_counter +=1
	else:
		naughty_counter +=1

	return nice_counter, naughty_counter

def pair_checker(word):
	bi_word_list = [word[i:(i+2%len(word))] for i in range(len(word)-2)]
	for _ ,val in enumerate(bi_word_list):
		bi_word_list.remove(val)
		if val in bi_word_list:
			return True
	return False

def triad_checker(word):
	tri_word_list = [word[i:(i+3%len(word))] for i in range(len(word)-2)]
	for i in tri_word_list:
		if len(i) > 1:
			if i[0] == i[-1]:
				return True
	return False

# application
f = open('inp.txt').read().splitlines()
nice_counter = 0
naughty_counter = 0

for word in f:
	nice_counter, naughty_counter = nice_discriminator(word, nice_counter, naughty_counter)

print(f'nice:{nice_counter}, naughty:{naughty_counter}')

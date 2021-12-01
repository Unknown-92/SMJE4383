def are_anagrams(word1, word2):
	word1_sorted = sorted(word1)
	word2_sorted = sorted(word2)
	
	return word1_sorted == word2_sorted # Check that the sorted words are identical


print("Anagram Test")

valid_input_boll = False
while not valid_input_bool:
	try:
		two_words = input("Enter two space seperated words: ")
		# Chage all latter to lower caps
		two_words = two_words.lower() 
		word1,word2 = two_words.split()
		
		valid_input_bool = True
	except ValueError:
		print("Bad input")


if are_anagrams(word1,word2): # Return True or False
	print("The words {} and {} are anagrams.".format(wor1, word2))
else:
	print("The words are {} and {} not anagrams.".format(wor1, word2))

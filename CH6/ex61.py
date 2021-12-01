def are_anagrams(word1, word2):
	word1_sorted = sorted(word1)
	word2_sorted = sorted(word2)
	
	return word1_sorted == word2_sorted # Check that the sorted words are identical


print("Anagram Test")

two_words = input("Enter two space seperated words: ")
# Chage all latter to lower caps
two_words = two_words.lower() 
word1,word2 = two_words.split()

if are_anagrams(word1,word2): # Return True or False
	print("The words are anagrams.")
else:
	print("The words are not anagrams.")

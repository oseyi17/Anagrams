# Check if two words are an anagrams 
from collections import Counter

def find_anagrams(word1, word2):
    word1 = "".join(word1.split(" "))
    word2 = ''.join(word2.split(" "))
    return sorted(word1)==sorted(word2)
    
print(find_anagrams("hello", "helle"))
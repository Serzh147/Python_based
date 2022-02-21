from collections import Counter
str1 = "кот"
str2 = "ток"
def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)
anagrams("abc1", "1bac") # True
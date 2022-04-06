b = input()
def get_vowels(String):
    return [each for each in String if each in "aeiou"]
get_vowels("animal") # [a, i, a]
get_vowels("why") # []
get_vowels("football") # [o, o, a]
print(get_vowels(b))

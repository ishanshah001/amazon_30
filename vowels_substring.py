def countVowels(self, word: str) -> int:
    vowels = set(['a','e','i','o','u'])
    sum = 0
    for i,ch in enumerate(word):
        if ch in vowels:
            sum += (i + 1) * (len(word) - i)
    return sum
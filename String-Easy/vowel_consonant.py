class Solution:
    def countVowelsAndConsonants(self, s):
        vowels = "aeiou"
        vowel_count = 0
        consonant_count = 0

        for char in s:
            if char.isalpha():  # Ignore digits/symbols
                ch = char.lower()
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

        return vowel_count, consonant_count


if __name__ == "__main__":
    s = input("Enter a string: ")
    sol = Solution()
    vowels, consonants = sol.countVowelsAndConsonants(s)
    print("Vowels:", vowels)
    print("Consonants:", consonants)

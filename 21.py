word = input("Enter any word : ")
palindromes = ("radar","wow")
if word == word[::-1]:
    palindromes += (word,)

print(palindromes)

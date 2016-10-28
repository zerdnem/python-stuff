vowels = ['a', 'e', 'i', 'o', 'u']
letters = []
word = input("Please enter a word: ")
for w in word:
    letters.append(w)
x = []
for l in letters:
    if l in vowels:
        x.append(l)
print(x)
# print(list(set(letters).intersection(set(vowels))))
# print([l for l in letters if l in vowels])

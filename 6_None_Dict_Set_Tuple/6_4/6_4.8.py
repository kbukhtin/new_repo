from string import ascii_lowercase

alphabet = {}

for i in range(len(ascii_lowercase)):
    alphabet[ascii_lowercase[i]] = i + 1

print(alphabet)

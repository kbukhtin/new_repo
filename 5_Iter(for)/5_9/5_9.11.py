phrase = 'Take only the words that start with t in this sentence'

x = [i for i in phrase.split() if i[0] in ("tT")]
print(x)
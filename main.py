original = "PASTE YOUR WORD TO ENCRYPT HERE (NOT IN CAPS!!)"
key = "PASTE YOUR KEY HERE (NOT IN CAPS!!)"


# IF NECESSARY CHANGE THE DICTIONARY (SHOULD NOT BE NECESSARY9
my_dict = {
    " ": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    ".": 27,
}

# my_dict2 = dict((y, x) for x, y in my_dict.iteritems())
my_dict2 = {my_dict[k]: k for k in my_dict}
res = ""
for i in range(len(original)):
    temp = (my_dict[original[i]] - my_dict[key[i % len(key)]]) % 28
    res += (my_dict2[temp])
    # res = res + temp


# OUTPUTS THE ORIGINAL UNENCRYPTED WORD
print(res)

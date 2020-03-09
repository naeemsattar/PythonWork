import string

def ispangram(str, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet <= set(str.lower())

print(ispangram("A quick brown fox jumps over a white lazy dog."))
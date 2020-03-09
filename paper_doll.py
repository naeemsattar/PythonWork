# Return the 3 letters of each original given letter in the string.
def paper_doll(givenstr):
    answer = ''
    for item in givenstr:
        answer = answer + item*3;
    print(answer)


paper_doll("ThreeLetters")

# check either given string is PALINDROME or NOT

def palindrome(str):
    if(str == str[::-1]):
        print("Palindrome")
    else:
        print ("Not")


palindrome("madam")
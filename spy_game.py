# write a function that takes integers as input and return True if the numbers contains 007 in the order.

def spy_game(nums):
    compare = [0,0,7,'end']
    for x in nums:
        if x == compare[0]:
            compare.pop(0)
    if compare[0]=='end':
        return True
    else:
        return False


print(spy_game([1,0,0,4,7]))
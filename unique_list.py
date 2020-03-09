# Take a list and return the unique list
def unique_list(lst):
    uni_lst = []
    for x in lst:
        if x not in uni_lst:
            uni_lst.append(x)

    return uni_lst


print(unique_list([1,1,1,1,2,2,3,3,3,4,5,5,6,7,7,7]))




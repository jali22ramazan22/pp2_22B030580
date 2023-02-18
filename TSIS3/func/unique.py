def unique(lst1):
    lst1 = sorted(lst1)
    for i in range(0, len(lst1)):
        if i+1 < len(lst1):
            if lst1[i] == lst1[i+1]:
                lst1.pop(i+1)
    return lst1

lst1 = [1,5,5,2,2,10]
lst1 = unique(lst1)
print(lst1)

def has33(lst1):
    for i in range(0, len(lst1)):

        if i != (len(lst1) - 1):

            if lst1[i] == lst1[i + 1] and lst1[i] == 3:
                return True

    return False


print(has33([1, 3, 1, 3]))
def contains_007(lst):

    for i in range(len(lst)):

        if lst[i] == 0:

            if i+1 < len(lst) and lst[i+1] == 0:

                if i+2 < len(lst) and lst[i+2] == 7:

                    return True

    return False

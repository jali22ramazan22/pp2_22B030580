def palindrome(str1):
    str2 = ''.join(reversed(str1))
    if str2 == str1:
        print("YES")
    else:
        print("NO")

palindrome("MAM")

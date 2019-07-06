a = "clint eastwood"
b = "old west action"

def is_anagram(str1, str2):
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ", "")

    str1 = list(str1)
    str2 = list(str2)

    flag = 1

    if len(str1) != len(str2):
        flag = 0

    for i in str1:
        if i in str2:
            str2.remove(i)
        else:
            flag = 0

    if flag == 0:
        return False
    else:
        return True


def anagram(s1, s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Return boolean for sorted match.
    return sorted(s1) == sorted(s2)

print(is_anagram(a,b))
def compress(s):
    compressed_s = ""
    count = 1

    for i in range(1,len(s)):

        if s[i] == s[i-1]:
            count += 1

        else:
            compressed_s += s[i-1] + str(count)
            count = 1

        if i == (len(s) - 1):
            compressed_s += s[i] + str(count)
            count = 1


    return compressed_s


compress('AAABCCDDDDD')

def rev_word(s):
    s = s.strip()
    print(s)

    # s.replace(" ","")
    # print(s)

    print(" ".join(s.split()[::-1]))


rev_word('  Hi John,   are you ready to go?  ')

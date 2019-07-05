siz = int(input())
strings = input()
count = 0

for i in range(0,siz):
    for j in range(0, siz):
        if strings[j]>strings[i]:
            count += 1
    print(count)
    count = 0



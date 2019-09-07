def sum_no(num):
    sum = 0
    while num!=0:
        rem = num%10
        sum += rem
        num = num//10

    return sum


target = int(input())
a = target
max_num = target
multiplier = 1

while target != 0:

    current = (target-1) * multiplier + (multiplier - 1)
    # print(current)

    total = sum_no(current)

    if total > sum_no(max_num) or total == sum_no(max_num) and current >= max_num:
        max_num = current

    multiplier = multiplier * 10
    target = target//10

# print(max_num)


num = int(str(int(str(a)[0])-1) + '9' * (len(str(a))-1))
numm = list(str(num))
aa = list(str(a))
number = list(int(x) for x in aa)
number2 = list(int(x) for x in numm)

if sum(number) >= sum(number2):
    print(a)
else:
    print(num)


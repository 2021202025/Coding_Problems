def sum_no(num):
    sum = 0
    while num!=0:
        rem = num%10
        sum += rem
        num = num//10

    return sum


target = int(input())

max_num = target
multiplier = 1

while target != 0:

    current = (target-1) * multiplier + (multiplier - 1)
    print(current)

    total = sum_no(current)

    if total > sum_no(max_num) or total == sum_no(max_num) and current >= max_num:
        max_num = current

    multiplier = multiplier * 10
    target = target//10

print(max_num)


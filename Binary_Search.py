lis = [1,2,3,4,5,6,7,8,9]


mid = len(lis)//2
element = 8

flag = False
begin = 0
end = len(lis)

for i in range(begin, end):

    mid = (begin + end)//2

    if mid >= len(lis):
        break

    if lis[mid] == element:
        flag = True
        print("Iteration   " + str(i) + "   " + str(lis[mid]))
        break

    if lis[mid] < element:
        begin = mid + 1
        continue

    if lis[mid] > element:
        end = mid
        continue

if flag == False:
    print("Element not found")
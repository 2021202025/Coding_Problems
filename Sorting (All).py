lis = [1,5,2,7,3,1,56,23,5,6,9,3]
new_lis = []

def bubble_sort(lis):
    for i in range(len(lis)-2):
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                temp = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = temp

    return lis


print(bubble_sort(lis))

lis = [1,5,2,7,3,1,56,23,5,6,9,3]

def selection_sort(lis):
    for i in range(len(lis)-1):
        min_position = i
        for j in range(i, len(lis)):
            if lis[j] < lis[min_position]:
                min_position = j

        temp = lis[min_position]
        lis[min_position] = lis[i]
        lis[i] = temp

    return lis

print(selection_sort(lis))

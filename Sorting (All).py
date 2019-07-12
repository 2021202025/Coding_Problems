lis = [1,5,2,7,3,1,56,23,5,6,9,3]

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


lis = [1,5,2,7,3,1,56,23,5,6,9,3]


def insertion_sort(lis):
     for i in range(1,len(lis)):
        value = lis[i]
        pos = i

        while pos>0 and value < lis[pos-1]:

            lis[pos] = lis[pos-1]
            pos = pos-1

        lis[pos] = value

     return lis

print(insertion_sort(lis))

lis = [1,0,5,2,7,3,1,56,23,5,6,9,3]


def shell_sort(lis):

    sub_lis_count = len(lis)//2

    while sub_lis_count > 0:
        for start in range(sub_lis_count):
            gap_insertion_sort(lis,start,sub_lis_count)
        sub_lis_count = sub_lis_count//2

    return lis

def gap_insertion_sort(arr,start,gap):

    for i in range(start+gap, len(arr), gap):

        value = arr[i]
        pos = i
        while pos >= gap and arr[pos-gap] > value:
            arr[pos] = arr[pos-gap]
            pos = pos-gap

        arr[pos] = value


print(shell_sort(lis))
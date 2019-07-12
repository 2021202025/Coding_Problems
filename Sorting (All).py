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




lis = [1,5,2,7,3,1,56,23,5,6,9,3]


def merge_sort(lis):

    if len(lis) > 1:
        mid = len(lis)//2
        leftHalf = lis[:mid]
        rightHalf = lis[mid:]

        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i=0
        j=0
        k=0

        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                lis[k] = leftHalf[i]
                i += 1
            else:
                lis[k] = rightHalf[j]
                j += 1

            k += 1


        while i < len(leftHalf):
            lis[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            lis[k] = rightHalf[j]
            j += 1
            k += 1

    return lis

print(merge_sort(lis))

lis = [1,5,2,7,3,1,56,23,5,6,9,3]

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def mergesort(lst):
    if (len(lst) <= 1):
        return lst
    mid = int(len(lst) / 2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)

print(mergesort(lis))



lis = [1,5,2,7,3,1,56,23,5,6,9,3]

def quick_sort(lis):

    quick_sort_splits(lis, 0, len(lis)-1)
    return lis

def quick_sort_splits(lis, first, last):
    if first < last:
        splitpoint = quick_partition(lis, first, last)

        quick_sort_splits(lis, first, splitpoint-1)
        quick_sort_splits(lis, splitpoint+1, last)


def quick_partition(lis, first, last):
    pivot = lis[first]

    leftMark = first+1
    rightMark = last

    done = False

    while not done:

        while leftMark <= rightMark and lis[leftMark] <= pivot:
            leftMark += 1

        while rightMark >= leftMark and lis[rightMark] >= pivot:
            rightMark -= 1

        if rightMark < leftMark:
            done = True

        else:
            temp = lis[rightMark]
            lis[rightMark] = lis[leftMark]
            lis[leftMark] = temp

    temp = lis[first]
    lis[first] = lis[rightMark]
    lis[rightMark] = temp

    return rightMark

print(quick_sort(lis))
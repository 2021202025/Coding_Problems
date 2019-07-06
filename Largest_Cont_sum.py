def large_cont_sum(arr):
    largest_sum = 0
    for i in range(0,len(arr)):
        sum = arr[i]
        if sum > largest_sum:
            largest_sum = sum
        for j in range(i+1,len(arr)):
            sum += arr[j]

            if sum > largest_sum:
                largest_sum = sum

    print(largest_sum)



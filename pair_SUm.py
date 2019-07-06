def pair_sum(arr, k):
    count = 0
    req = 0
    gone_through = []

    for i in arr:
        req = k-i

        if req in arr:

            if i not in gone_through and req not in gone_through:
                count += 1

            gone_through.append(i)
            gone_through.append(req)

    print(count)

pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)


def pair_sum(arr, k):
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k - num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
            print(seen)

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))

    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    # return '\n'.join(map(str,list(output)))
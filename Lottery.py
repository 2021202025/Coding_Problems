def func(array):
    lottery = []
    final = []
    flag = False

    for i in range(len(array)):
        lottery.append(array[i])

        if len(lottery) == 1:
            final.append(lottery[0])
            continue

        for j in range(len(lottery)):
            for k in range(len(lottery)):
                if j!=k:
                    if array[j] == array[k]:
                        flag = False
                        break
                    else:
                        flag = True
                        continue

                # else:
                #     flag=True

            if flag:
                final.append(array[j])
                break
            elif(j==(len(lottery)-1)):
                final.append(-1)

    print(final)

    return




array = ['w','w','a','c','a']
func(array)
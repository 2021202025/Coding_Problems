def balance_check(s):
    stack = []
    flag = True

    for i in s:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)

        if i == ")" or i == "]" or i == "}":
            top = stack.pop()

            if i == ")" and top == "(":
                continue

            elif i == "]" and top == "[":
                continue

            elif i == "}" and top == "{":
                continue

            else:
                flag = False
                break

    if len(stack) != 0:
        return False

    return flag



print(balance_check('[](){([[[]]])}('))
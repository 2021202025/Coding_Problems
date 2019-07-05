siz = int(input())
strings = input()

new_string = ""

nos = list(int(s) for s in strings)

for i in range(0,siz):
    new_string += str(max(nos))
    nos.remove(max(nos))

print(new_string)
def primality(n):

    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

myList = []
for i in range(2, 101):
    if primality(i) == 1:
        myList.append(i)
print(myList)





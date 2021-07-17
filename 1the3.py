n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')



name = "привет"
x = 0
for i in name:
    x = x + 1
    print(name[0:x])
for i in name:
    x = x - 1
    print(name[0:x])


name_ofStars = "******"
y = 0
for i in name:
    y = y + 1
    print(name_ofStars[0:y])
for i in name:
    y = y - 1
    print(name_ofStars[0:y])

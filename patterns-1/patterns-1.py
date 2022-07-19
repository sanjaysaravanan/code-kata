n = int(input())

'''
n = 3
*
**
***

n = 5
*
**
***
****
*****
'''
# for i in range(1, n+1):
#     for j in range(0, i):
#         print("*", end='')
#     print()


'''
n = 3
1
22
333

n = 5
1
22
333
4444
55555
'''
# for i in range(1, n+1):
#     for j in range(0, i):
#         print(i, end='')
#     print()


'''
n = 3
1
21
321

n = 4
1
21
321
4321
'''
# for i in range(1, n+1):
#     for j in range(0, i):
#         print(i-j, end="")
#     print()

'''
n = 3
1
23
345

n = 4
1
23
345
4567
'''
# for i in range(1, n+1):
#     for j in range(0, i):
#         print(i+j, end="")
#     print()

'''
n = 3
1
23
456

n = 4
1
23
456
78910
'''
i = 1

while i <= n:
    j = 1
    p = 1
    while j <= i:
        print(p, end="")
        j = j + 1
        p = p + 1
    i = i + 1
    print()


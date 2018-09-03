import math
def sol(n):
    a = math.sqrt(n)
    c=0
    b = 0
    if int(a) == a:
        b = 4
    s = int(a-math.sqrt(a/2)+1)
    a = int(a)
    for i in range(s,a):
        j = (math.sqrt(n-i**2))
        if int(j)==j:
            print(i,j)
            c+=1
    return (b+c*8)
sum = 0
for i in [9, 567890000, 10000000000, 999999999, 123454321, 10000000000000 ]:
    sum += sol(i)
print(sum)

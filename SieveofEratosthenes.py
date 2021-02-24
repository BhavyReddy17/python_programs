requd_range = int(input("enter the range: "))
num = list(range(2,requd_range + 1))
for i in range(2,requd_range+1):
    for j in range(i ** 2,requd_range + 1):
        if (j%i == 0):
            if j not in num:
                continue
            num.remove(j)
print(num)
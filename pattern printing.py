a=7
for i in range(1,a+1):
    print("*" *(i if i<=a//2 + 1 else a - i + 1))

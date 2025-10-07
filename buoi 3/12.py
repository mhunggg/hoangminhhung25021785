n=int(input())
if n >= 100:
    print((n-100)*3000 + 175000)
else:
    if n >= 50:
        print((n-50)*2000 + 75000)
    else:
        print(n*1500)
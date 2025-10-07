a,b = map(float, input().split())
if a == b == 0:
    print("Vô số nghiệm")
else:
    if a == 0:
        print("Vô nghiệm")
    else:
        print("{0:.2f}".format(-b/a))
a, b = map(int, input("Nhập hai số a b: ").split())
a = a ^ b
b = a ^ b
a = a ^ b
print("Sau khi hoán đổi:", a, b)

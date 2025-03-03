def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Nhap vao soso: "))
if is_prime(num):
    print(f"{num} la so nguyen to.")
else:
    print(f"{num} kh phai la so nguyen to")
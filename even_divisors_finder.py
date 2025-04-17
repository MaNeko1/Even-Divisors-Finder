# GitHub: MaNeko1
n = int(input("n: "))
total = 0

for i in range(1, n+1):
    if n % i == 0 and i % 2 == 0:
        print(f"{i} หาร {n} ลงตัวและเป็นเลขคู่")
        total += i

print(f"{total} ผลรวม")
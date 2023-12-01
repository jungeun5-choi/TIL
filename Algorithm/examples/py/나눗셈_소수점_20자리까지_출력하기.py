a, b = input().split()

a = int(a)
b = int(b)

# 소수점 앞자리
print(f"{a // b}.", end='')

count = 20  # 소수점 뒤 20자리
for i in range(count):
  a *= 10
  print(a // b, end='')
  a %= b

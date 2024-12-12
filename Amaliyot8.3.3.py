#Amaliyot8.3.3
def kattasi(a, b, c):
    mx = 0
    mn = 0
    if a > b:
       mx = a
    else:
        mx = b
    if mx > c:
        return mx
    else:
        return c
a, b, c = map(int, input().split())
print(f"Uchta sonning kattasi: {kattasi(a, b, c)}")

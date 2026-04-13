import ctypes

test = ctypes.CDLL('./libtest.so')

test.calculate_primes.restype = None
test.calculate_primes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

print("введите n:")
n = int(input())
print("введите m:")
m = int(input())

primes = (ctypes.c_int * (m + 1))(*([0] * (m+1))) # создаем список (массив) на m+1 интовых элементов

test.calculate_primes(primes, m)

k = n
while k <= m:
    c = 0
    x1 = 0
    y1 = 0
    
    for x in range(2, k // 2 + 1):
        if primes[x] and primes[k - x]:
            c = c + 1
            if x1 == 0:
                x1 = x
                y1 = k - x
    
    print(k, c, x1, y1)
    k = k + 2
# Дополнительный импорт

# Дополнительный импорт

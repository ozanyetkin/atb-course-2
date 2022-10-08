# n basamakli butun binary sayi ihtimallerini verecek bir fonksiyon
# n = 2 => ["00", "01", "10", "11"]
# n = 3 => ["000", "001", "010", "011", "101", "110", "100", "111"]

def n_binary(n):
    binaries = [""]
    if n == 0:
        return [""]
    else:
        for binary in n_binary(n - 1):
            binaries.append(binary + "1")
            binaries.append(binary + "0")
        binaries.reverse()
        return binaries[:2 ** n]

print(n_binary(5))

def n_binary(n, binaries=""):
    if n == 0:
        return [binaries]
    else:
        return n_binary(n - 1, binaries="0" + binaries) + n_binary(n - 1, binaries="1" + binaries)

a = n_binary(3)
a.sort()
print(a)
from math import floor

def dec_to_bin(x):
    c = floor(x)
    u = x - c
    c_prim = ""

    while c > 0:
        c_prim = str(c % 2) + c_prim
        c //= 2

    MAX_ITER = 8
    ITER = 0
    u_prim = ""

    while u != 0:
        u *= 2
        u_prim += str(floor(u))
        u = u - floor(u)
        ITER += 1
        if ITER > MAX_ITER:
            break

    if len(c_prim) == 0:
        c_prim = "0"

    if len(u_prim) == 0:
        u_prim = "0"

    return c_prim + "," + u_prim

print("== Decimal to Binary ==")
print(dec_to_bin(10.533))
print(dec_to_bin(1/3))

def bin_to_dec(x):
    ind = len(x)

    if ',' in x:
        ind = x.index(',')

    x = x.replace(",", "")
    pw = ind - len(x)
    x_s = 0

    for x_i in x[::-1]:
        x_s += 2 ** pw * int(x_i)
        pw += 1

    return x_s

print("== Binary to Decimal ==")
print(bin_to_dec("101,11011"))
print(bin_to_dec("011010000100"))

def dec_to_hex(x):
    c = floor(x)
    u = x - floor(x)
    NUMBERS = "0123456789ABCDEF"
    c_prim = ""

    while c > 0:
        c_prim = NUMBERS[c % 16] + c_prim
        c //= 16

    MAX_ITER = 8
    ITER = 0
    u_prim = ""

    while u != 0:
        u *= 16
        u_prim += NUMBERS[floor(u)]
        u -= floor(u)
        ITER += 1

        if ITER > MAX_ITER:
            break

    if len(c_prim) == 0:
        c_prim = "0"

    if len(u_prim) == 0:
        u_prim = "0"

    return c_prim + "," + u_prim

print("== Decimal to Hexadecimal ==")
print(dec_to_hex(21481))
print(dec_to_hex(16.78))

def hex_to_dec(x):
    ind = len(x)

    if ',' in x:
        ind = x.index(',')

    x = x.replace(",", "")
    NUMBERS = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }
    pw = ind - len(x)
    x_s = 0

    for x_i in x[::-1]:
        x_s += 16 ** pw * NUMBERS[x_i]
        pw += 1

    return x_s

print("== Hexadecimal to Decimal ==")
print(hex_to_dec("ACDC,73"))
print(hex_to_dec("CF875,AA4"))

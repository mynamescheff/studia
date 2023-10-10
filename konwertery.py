import math

def decimal_to_binary(decimal_number):
    whole_part = math.floor(decimal_number)
    fractional_part = decimal_number - whole_part
    binary_whole = ""
    
    while whole_part > 0:
        binary_whole = str(whole_part % 2) + binary_whole
        whole_part //= 2

    MAX_ITER = 8
    ITER = 0
    binary_fractional = ""

    while fractional_part != 0:
        fractional_part *= 2
        binary_fractional += str(math.floor(fractional_part))
        fractional_part -= math.floor(fractional_part)
        ITER += 1

        if ITER > MAX_ITER:
            break

    if len(binary_whole) == 0:
        binary_whole = "0"

    if len(binary_fractional) == 0:
        binary_fractional = "0"

    return binary_whole + "," + binary_fractional

print("Decimal to Binary")
print(decimal_to_binary(10.533))
print(decimal_to_binary(1/3))

def binary_to_decimal(binary_number):
    index = len(binary_number)

    if ',' in binary_number:
        index = binary_number.index(',')

    binary_number = binary_number.replace(",", "")
    power = index - len(binary_number)
    decimal_number = 0

    for digit in binary_number[::-1]:
        decimal_number += 2 ** power * int(digit)
        power += 1

    return decimal_number

print("Binary to Decimal")
print(binary_to_decimal("101,11011"))
print(binary_to_decimal("011010000100"))

def decimal_to_hexadecimal(decimal_number):
    whole_part = math.floor(decimal_number)
    fractional_part = decimal_number - whole_part
    HEX_DIGITS = "0123456789ABCDEF"
    hex_whole = ""

    while whole_part > 0:
        hex_whole = HEX_DIGITS[whole_part % 16] + hex_whole
        whole_part //= 16

    MAX_ITER = 8
    ITER = 0
    hex_fractional = ""

    while fractional_part != 0:
        fractional_part *= 16
        hex_fractional += HEX_DIGITS[math.floor(fractional_part)]
        fractional_part -= math.floor(fractional_part)
        ITER += 1

        if ITER > MAX_ITER:
            break

    if len(hex_whole) == 0:
        hex_whole = "0"

    if len(hex_fractional) == 0:
        hex_fractional = "0"

    return hex_whole + "," + hex_fractional

print("Decimal to Hexadecimal")
print(decimal_to_hexadecimal(21481))
print(decimal_to_hexadecimal(16.78))

def hexadecimal_to_decimal(hexadecimal_number):
    index = len(hexadecimal_number)

    if ',' in hexadecimal_number:
        index = hexadecimal_number.index(',')

    hexadecimal_number = hexadecimal_number.replace(",", "")
    HEX_DIGITS = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }
    power = index - len(hexadecimal_number)
    decimal_number = 0

    for digit in hexadecimal_number[::-1]:
        decimal_number += 16 ** power * HEX_DIGITS[digit]
        power += 1

    return decimal_number

print("Hexadecimal to Decimal")
print(hexadecimal_to_decimal("ACDC,73"))
print(hexadecimal_to_decimal("CF875,AA4"))
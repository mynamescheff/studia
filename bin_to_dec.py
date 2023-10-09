def binary_to_decimal(binary_str):
    #sprawdzić czy jest przecinek w stringu
    if '.' in binary_str:
        integer_part, fractional_part = binary_str.split('.')
        integer_decimal = 0
        fractional_decimal = 0.0

        #przez przecinkiem
        for i in range(len(integer_part)):
            bit = int(integer_part[i])
            integer_decimal += bit * 2**(len(integer_part) - i - 1)

        #po przecinku
        for i in range(len(fractional_part)):
            bit = int(fractional_part[i])
            fractional_decimal += bit * 2**(-(i + 1))

        return integer_decimal + fractional_decimal
    else:
        decimal_value = 0
        for i in range(len(binary_str)):
            bit = int(binary_str[i])
            decimal_value += bit * 2**(len(binary_str) - i - 1)
        return decimal_value

#Przykład użycia:
binary_str = "11100100101.0111010010"
decimal_value = binary_to_decimal(binary_str)
print(f"The decimal equivalent of {binary_str} is {decimal_value}")

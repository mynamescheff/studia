def decimal_to_binary(decimal_number):
    # Split the number into integer and fractional parts
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part

    # Convert the integer part to binary
    binary_integer = bin(integer_part).replace("0b", "")

    # Convert the fractional part to binary
    binary_fractional = ""
    precision = 10  # Adjust this for desired precision

    while fractional_part > 0 and precision > 0:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional += str(bit)
        fractional_part -= bit
        precision -= 1

    # Combine the integer and fractional parts
    binary_result = binary_integer
    if binary_fractional:
        binary_result += "." + binary_fractional

    return binary_result

# Example usage
decimal_number = 13.375
binary_representation = decimal_to_binary(decimal_number)
print("Binary representation of", decimal_number, "is:", binary_representation)
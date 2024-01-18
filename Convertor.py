def convert_from_decimal(number, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    if number == 0:
        return '0'
    sign = -1 if number < 0 else 1
    number *= sign
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    while number > 0:
        number, remainder = divmod(number, base)
        result += digits[remainder]
    if sign == -1:
        result += '-'
    return result[::-1]


def convert_to_decimal(number, base):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = str(number).upper()
    if number[0] == '-':
        sign = -1
        number = number[1:]
    else:
        sign = 1
    result = 0
    for digit in number:
        if digit not in digits[:base]:
            raise ValueError("Number contains invalid digits for the base")
        result = result * base + digits.index(digit)
    return sign * result

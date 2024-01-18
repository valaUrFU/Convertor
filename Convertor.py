def convert_from_decimal(number, base):
    """
    Конвертирует число из десятичной системы счисления в заданную.

    Параметры:
    number (int): Число в десятичной системе счисления.
    base (int): Система счисления, в которую нужно перевести число. Должна быть от 2 до 36.

    Возвращает:
    str: Число в заданной системе счисления.
    """
    # Проверяем, что основание системы счисления в допустимом диапазоне
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    # Если число равно нулю, возвращаем '0'
    if number == 0:
        return '0'
    # Определяем знак числа
    sign = -1 if number < 0 else 1
    # Приводим число к положительному значению
    number *= sign
    # Строка с возможными цифрами
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    # Пока число больше нуля, делим его на основание системы счисления и добавляем остаток в результат
    while number > 0:
        number, remainder = divmod(number, base)
        result += digits[remainder]
    # Если число было отрицательным, добавляем минус к результату
    if sign == -1:
        result += '-'
    # Возвращаем перевернутый результат
    return result[::-1]


def convert_to_decimal(number, base):
    """
    Конвертирует число из заданной системы счисления в десятичную.

    Параметры:
    number (str): Число в заданной системе счисления.
    base (int): Система счисления числа. Должна быть от 2 до 36.

    Возвращает:
    int: Число в десятичной системе счисления.
    """
    # Проверяем, что основание системы счисления в допустимом диапазоне
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    # Строка с возможными цифрами
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Приводим число к верхнему регистру
    number = str(number).upper()
    # Определяем знак числа
    if number[0] == '-':
        sign = -1
        number = number[1:]
    else:
        sign = 1
    result = 0
    # Для каждой цифры числа умножаем текущий результат на основание системы счисления и добавляем значение цифры
    for digit in number:
        if digit not in digits[:base]:
            raise ValueError("Number contains invalid digits for the base")
        result = result * base + digits.index(digit)
    # Возвращаем результат с учетом знака
    return sign * result

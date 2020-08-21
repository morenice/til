def to_base62(number):
    base62_map = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    quotient = number
    remainder = 0

    result = []
    while number >= 62:
        quotient = int(number / 62)
        remainder = int(number % 62)

        result.insert(0, base62_map[remainder])
        number = quotient

    result.insert(0, base62_map[quotient])
    return ''.join(result)


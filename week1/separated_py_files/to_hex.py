def to_hex(decimal_number, leading_zeros=False):
    if decimal_number < 0 or decimal_number > 255:
        return None
    
    hex = {key + 10: chr(ord('a') + key) for key in range(0, 6)}
    
    def get_hex(number):
        if number < 10:
            return str(number)
        return str(hex[number])
    
    if decimal_number < 16 and not leading_zeros:
        return get_hex(decimal_number)
    
    hex_string = get_hex(decimal_number // 16) + get_hex(decimal_number % 16)

    return hex_string


def hex_color(red,green,blue):
    return f'#{to_hex(red, True)}{to_hex(green, True)}{to_hex(blue, True)}'

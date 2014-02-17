
def binary_translate(n):
    binary_str = str(n)
    binary_list = []
    place_value = 1
    dec_value = 0

    for digit in binary_str:
        binary_list.append(int(digit))

    while len(binary_list) > 0:
        current_place = binary_list.pop()
        dec_value += place_value * current_place
        place_value *= 2

    return dec_value


def solve_flag():
    # Known values
    known_values = {
        1: 110,  # 'n'
        2: 48,  # '0'
        3: 48,  # '0'
        4: 98,  # 'b'
        5: 122,  # 'z'
        6: 123,  # '{'
        24: 125,  # '}'
    }

    known_values[8] = known_values[1] ^ 22
    known_values[10] = 176 - known_values[24]
    known_values[22] = known_values[6] ^ 23

    #(Asc(char_12) / 5) ^ (Asc(char_3) / 12) = 130321
    known_values[12] = ((known_values[3] // 12) ^ 130321) * 5

    known_values[15] = int(14040 / known_values[8])

    # If Asc(char_12) Xor (Asc(char_17) + 5) = 5 Then
    known_values[17] = (5 ^ known_values[12]) - 5
    known_values[14] = 77 ^ known_values[24]
    known_values[13] = 73 ^ known_values[14] ^ known_values[2]
    known_values[22] = 1365 ^ 1337
    known_values[21] = known_values[22]
    known_values[11] = known_values[22]
    known_values[7] = known_values[10]
    known_values[23] = 235 - known_values[8]
    known_values[18] = known_values[23]

    #observation
    known_values[17] = ord('_')
    known_values[12] = ord('_')
    known_values[13] = ord('y')

    known_values[16] = known_values[17] + 19
    known_values[19] = 107
    known_values[20] = (known_values[1] * 5) - 501
    known_values[9] = -9 + known_values[22]

    for key, v in sorted(known_values.items()):
        print(key, chr(v))

    flag_chars = {i: known_values.get(i, 32) for i in range(1, 25)}
    flag = ''.join(chr(flag_chars[i]) for i in range(1, 25))
    return flag


print("Flag:", solve_flag())

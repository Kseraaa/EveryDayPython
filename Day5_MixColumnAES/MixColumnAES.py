import numpy as np

def galois_multiply(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        carry = a & 0x80
        a <<= 1
        if carry:
            a ^= 0x1b
        b >>= 1
    return p % 256

def mix_single_column(col):
    fixed = [2, 3, 1, 1]
    temp = []
    for i in range(4):
        temp.append(galois_multiply(col[0], fixed[i]) ^
                    galois_multiply(col[1], fixed[(i + 1) % 4]) ^
                    galois_multiply(col[2], fixed[(i + 2) % 4]) ^
                    galois_multiply(col[3], fixed[(i + 3) % 4]))
    return temp

state = [
    [0x63, 0xC9, 0xFE, 0x30],
    [0xF2, 0x63, 0x26, 0xF2],
    [0x7D, 0xD4, 0xC9, 0xC9],
    [0xD4, 0xFA, 0x63, 0x82]
]

# Transpose to get columns
state = np.array(state).T

new_state = np.zeros((4, 4), dtype=int)
for i in range(4):
    new_state[i] = mix_single_column(state[i])

# Transpose back to original row-column order
new_state = new_state.T

new_state_hex = np.vectorize(lambda x: format(x, '02X'))(new_state)

print(new_state_hex)

def decode(encoded_passcode):
    decoded_passcode = ""

    for m in encoded_passcode:
        m = int(m)
        if m >= 3:
            m -= 3
            decoded_passcode += str(m)
        else:
            m = 10 + m - 3
            decoded_passcode += str(m)

    return decoded_passcode
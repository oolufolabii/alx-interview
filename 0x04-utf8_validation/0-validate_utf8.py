#!/usr/bin/python3

"""Python module for UFT-8 validator"""


def validUTF8(data):
    """Checking if a list of integers are valid UFT-8 code points"""
    count = 0
    data_len = len(data)
    for i in range(data_len):
        if count > 0:
            count -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            count = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            byte_span = 4
            if data_len - i >= byte_span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte_span],
                ))
                if not all(next_body):
                    return False
                count = byte_span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            byte_span = 3
            if data_len - i >= byte_span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte_span],
                ))
                if not all(next_body):
                    return False
                count = byte_span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte encoding
            byte_span = 2
            if data_len - i >= byte_span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte_span],
                ))
                if not all(next_body):
                    return False
                count = byte_span - 1
            else:
                return False
        else:
            return False
    return True

import sys

#a
def encode_text(text, key):
    s = int(key)
    for ch in text:
        ch3 = ord(ch)
        if ch3 <= 90 and ch3 >= 65:
            ch3 = int(ord(ch)) + s
            if ch3 > 90:
                ch3 =ch3 - 26
            elif ch3 < 65:
                ch3 = ch3 + 26
            else:
                ch3 = ch3
        elif ch3 <= 122 and ch3 >= 97:
            ch3 = int(ord(ch)) + s
            if ch3 > 122:
                ch3 = ch3 - 26
            if ch3 < 97:
                ch3 = ch3 + 26
            else:
                ch3 = ch3
        encode_text =chr(ch3)
        print(encode_text, end = "")

if __name__ == "__main__":
    text = sys.argv[1]
    key = sys.argv[2]
    encode_text(text, key)

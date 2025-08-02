def text_to_ascii(text):
    return [str(ord(c)) for c in text]

def text_to_bin(text):
    return [format(ord(c), '08b') for c in text]

def text_to_hex(text):
    return [format(ord(c), '02x') for c in text]

def text_to_dec(text):
    return [str(ord(c)) for c in text]

def ascii_to_text(seq):
    try:
        return ''.join([chr(int(n)) for n in seq.strip().split()])
    except:
        return "[Invalid ASCII input]"

def bin_to_text(seq):
    try:
        chars = seq.strip().split()
        return ''.join([chr(int(b, 2)) for b in chars])
    except:
        return "[Invalid binary input]"

def hex_to_text(seq):
    try:
        chars = seq.strip().split()
        return ''.join([chr(int(h, 16)) for h in chars])
    except:
        return "[Invalid hex input]"

def dec_to_text(seq):
    try:
        chars = seq.strip().split()
        return ''.join([chr(int(d)) for d in chars])
    except:
        return "[Invalid decimal input]"
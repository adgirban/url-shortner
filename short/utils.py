import random
import string

def generate_key(length):
    chars = string.ascii_letters + string.digits
    result = ""
    i = 0
    while i < length:
        result = result + random.choice(chars)
        i = i + 1
    return result

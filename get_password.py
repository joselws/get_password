from random import choice
import sys

def get_password():
    pass_length = int(sys.argv[1])
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_!@#$%&*.?'
    password = ''
    while len(password) < pass_length:
        password += choice(chars)
    print(password)


if __name__ == "__main__":
    get_password()
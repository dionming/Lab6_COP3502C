from EncoderDionM import encode
from decoder import decoder

def menu():
    print('1. Encoder')
    print('2. Decoder')
    print('3. Exit')

def main():

    while True:
        menu()
        menuop = input('Select an option: ')

        if menuop == 1:
            passwd = input('Input a password to be encoded: ')
            encpass = encode(passwd)
        if menuop == 2:
            password = input('Input a password to be decoded: ')
            decoded = decoder(password)
        if menuop == 3:
            break


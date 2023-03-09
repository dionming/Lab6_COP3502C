from EncoderDionM import encode

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

        if menuop == 3:
            break
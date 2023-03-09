from EncoderDionM import encode
from decoder import decoder

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def main():

    while True:
        print()
        menu()
        print()
        menuop = input('Please enter an option: ')

        if menuop == '1':
            passwd = input('Input a password to be encoded: ')
            encpass = encode(passwd)
            print('Your password has been encoded and stored!')
        if menuop == '2':
            decodepass = decoder(encpass)
            print('The encoded password is', encpass, end = '')
            print(', and the original password is', decodepass, end  = '.')
        if menuop == '3':
            break

main()
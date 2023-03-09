#Dion Ming.

def encode(pw):
    newpw = ''
    for i in pw:
        num = int(i)+3
        newpw += str(num)
    #print(newpw)
    return newpw


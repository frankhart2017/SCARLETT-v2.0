def decrypt(msg):
    decoded = []
    for i in range(0,len(msg)):
        if(i%2 == 0):
            decoded.append(chr(ord(msg[i])-2))
        else:
            decoded.append(chr(ord(msg[i])+3))
    return ''.join(decoded)

def performDecryption():
    # Get the private Key
    priKey = open("prikey.txt").read().split()
    # Get the encrypted text
    encrypted_text= bin(int(open("ctext.txt").read()))[2:]
    # Get the p g d
    _p= int(priKey[0])
    _g= int(priKey[1])
    _d= int(priKey[2])

    # Add passing
    padding= 32 - (len(encrypted_text) % 32)
    padding= padding%32
    # Get the encrypted binary string
    binaryEncryptedString= '0'*padding + encrypted_text
    number_of_blocks= len(binaryEncryptedString) // 64
    decrypted_text = ""
    # Read string
    for i in range(number_of_blocks):
        encrypted_text= binaryEncryptedString[64*i:64*i + 64]
        
        temp= (pow(int(encrypted_text[0:32], 2), _p-1-_d, _p) * int(encrypted_text[32:], 2))
        temp= temp%_p

        decrypted_text +=  chr(temp & 0xFF) + chr((temp & 0xFF00) >> 8) + chr((temp & 0xFF0000) >> 16) + chr((temp & 0xFF000000) >> 24)
        

    open("dtext.txt", 'w').write(decrypted_text)
    print ("Decrypted text = ", decrypted_text)
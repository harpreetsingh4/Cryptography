import key as k
import encrypt as e
import decrypt as d
import random
def main():
    while 1:
        print("Please enter one of the following options")
        print("k - Generate Public and Private Keys")
        print("e - Text Encryption (Keys Must Be Generated First)")
        print("d - Text Decryption (Key Must be generated and encrytpion performed)")
        print("q - quit")
        option = input("\n").lower()

        

        if option == 'k':
            print("please enter a number for seed generation")
            seedNumber= input("\n")
            random.seed(seedNumber)

            print("your keys")
            k.keyGenerator()
            print("\n")

        elif option == 'e':
            e.encryption()
            print("\n")

        elif option == 'd':
            
            d.performDecryption()
            print("\n")
        elif option == 'q':
            return
        else:
            print("invalid option entered")
            print("\n")

main()

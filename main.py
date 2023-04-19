#!/usr/bin/env python3

import rsa

if __name__ == "__main__":
    quit = 0 # set to 1 to quit program
    pubKey, privKey = None, None # set to None to make it easy to check if the keys are set

    while quit != 1:
        print("What would you like to do?")
        # get user input in lowercase
        userInput = input("(G)enerate keys, (W)rite to file, (L)oad from file, (E)ncrypt, (D)ecrypt, (Q)uit: ").lower()
        if userInput == "g":
            pubKey, privKey = rsa.genKeys(1024, 40)
            print("pubKey: {}\nprivKey: {}".format(pubKey, privKey))
            print("Keys generated!")
        elif userInput == "w":
            print()
        elif userInput == "l":
            print()
        elif userInput == "e":
            if pubKey == None or privKey == None:
                print("Error: The keys are not defined. Please either generate keys or load them from files.")
                continue
            else:
                plaintext = input("Enter a message to encrypt: ")
                print(rsa.encrypt(plaintext, pubKey))
        elif userInput == "d":
            if pubKey == None or privKey == None:
                print("Error: The keys are not defined. Please either generate keys or load them from files.")
                continue
            else:
                ciphertext = [int(x) for x in input("Paste the encrypted data (without the brackets): ").split()]

                # convert the list of strings to integers
                #i = 0
                #while i <= len(ciphertext):
                #    ciphertext[i] = int(ciphertext[i])
                #    i += 1

                print(rsa.decrypt(ciphertext, privKey))
        elif userInput == "q":
            quit = 1
        else:
            print("Error: unknown option:", userInput)
            exit(1)

#!/usr/bin/env python3

import rsa

def readKey(keyFile):
    # read a key from a specified file

    # open, read, and close the file
    file = open(keyFile, 'r')
    key = [int(x) for x in file.read().split(', ')]
    file.close()
    return key

def writeKey(keyFile, key):
    # write a key to a specified file

    # open, write, and close the file
    file = open(keyFile, 'w')
    file.write('{0}, {1}'.format(key[0], key[1]))
    file.close()
    return 0

def readData(encryptedFile):
    # read encrypted data from a specified file

    # open, read, and close the file
    file = open(encryptedFile, 'r')
    encryptedData = [int(x) for x in file.read().split(', ')]
    file.close()
    return encryptedData

def writeData(encryptedFile, encryptedData):
    # write encrypted data to a specified file

    # open, write, and close the file
    file = open(encryptedFile, 'w')
    file.write(', '.join(str(char) for char in encryptedData))
    file.close()
    return 0


if __name__ == "__main__":
    quit = 0 # set to 1 to quit program
    pubKey, privKey = None, None # set to None to make it easy to check if the keys are set

    while quit != 1:
        print("What would you like to do?")
        # get user input in lowercase
        userInput = input("(G)enerate keys, (W)rite keys to file, (L)oad keys from file, (E)ncrypt, (D)ecrypt, (Q)uit: ").lower()
        if userInput == "g": # generate keys
            pubKey, privKey = rsa.genKeys(1024, 40)
            print("pubKey: {}\nprivKey: {}".format(pubKey, privKey))
            print("Keys generated!")

        elif userInput == "w": # write current keys to file
            if pubKey == None or privKey == None: # keys are not set
                print("Error: The keys are not defined. Please either generate keys or load them from files.")
            else: # keys are set
                # get file names from user input
                pubFile = input("Where would you like to store the public key? ['pubKey']: ")
                privFile = input("Where would you like to store the private key? ['privKey']: ")

                # write pubKey to file
                if pubFile == "": # default to 'pubKey'
                    print("writing pubKey to: 'pubKey'")
                    writeKey('pubKey', pubKey)
                else:
                    print("writing pubKey to: '{}'".format(pubFile))
                    writeKey(pubFile, pubKey)

                # write privKey to file
                if privFile == "": # default to 'privKey'
                    print("writing privKey to: 'privKey'")
                    writeKey('privKey', privKey)
                else:
                    print("writing privKey to: '{}'".format(privFile))
                    writeKey(privFile, privKey)

        elif userInput == "l": # load keys from file
            # get file names from user input
            pubFile = input("Where is the public key located? ['pubKey']: ")
            privFile = input("Where is the private key located? ['privKey']: ")

            # load pubKey from file
            if pubFile == "": # default to 'pubKey'
                print("loading pubKey from: 'pubKey'")
                pubKey = readKey('pubKey')
            else:
                print("loading pubKey from: '{}'".format(pubFile))
                pubKey = readKey(pubFile)

            # load privKey from file
            if privFile == "": # default to 'privKey'
                print("loading privKey from: 'privKey'")
                privKey = readKey('privKey')
            else:
                print("loading privKey from: '{}'".format(privFile))
                privKey = readKey(privFile)

        elif userInput == "e": # encrypt data (and save to a file)
            if pubKey == None or privKey == None: # keys are not set
                print("Error: The keys are not defined. Please either generate keys or load them from files.")
                continue
            else: # keys are set
                plaintext = input("Enter a message to encrypt: ")
                ciphertext = rsa.encrypt(plaintext, pubKey)
                print("Encrypted data: {}".format(ciphertext))

                # save encrypted data to a file
                encryptedFile = input("Where do you want to save the encrypted data? ['encryptedData']: ")

                if encryptedFile == "": # default to 'encryptedData'
                    print("writing encrypted data to: 'encryptedData'")
                    writeData('encryptedData', ciphertext)
                else:
                    print("writing encrypted data to: '{}'".format(encryptedFile))
                    writeData(encryptedFile, ciphertext)

        elif userInput == "d": # decrypt data
            if pubKey == None or privKey == None: # keys are not set
                print("Error: The keys are not defined. Please either generate keys or load them from files.")
                continue
            else: # keys are set
                encryptedFile = input("Where is the encrypted data located? ['encryptedData']: ")

                if encryptedFile == "": # default to 'encryptedData'
                    ciphertext = readData('encryptedData')
                else:
                    ciphertext = readData(encryptedFile)

                # decrypt and display data
                plaintext = rsa.decrypt(ciphertext, privKey)
                print("Decrypted message: {}".format(plaintext))

        elif userInput == "q": # quit the program
            quit = 1

        else: # the user has entered an unknown option
            print("Error: unknown option:", userInput)

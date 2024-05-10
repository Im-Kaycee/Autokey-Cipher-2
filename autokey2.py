"""Encryption:
1.Create dictionary for the letters
2. Input plain text
3. Input Key
4. Generate autokey
5. Match Pt to Ak
6. Create encryption algorithm
7. Output the Ct as letters
"""

import argparse


def main():
    # Create dictionary of letters
    Letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
               "M": 12,
               "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
               "Y": 24, "Z": 25}

    def encryption():
        parser = argparse.ArgumentParser()
        # Put in the plain text
        print("Welcome!!!!!!!!")
        parser.add_argument('-plaintext', '-p', help='This is the plaintext to be encrypted')
        parser.add_argument('-key', '-k', help='This is the key to be encrypt with')
        args = parser.parse_args()
        print(args.plaintext)
        plaintext = args.plaintext

        #plainText = input("Input plaintext: ").upper()
        # Input the key
        #key = input("What is the key: ").upper()

        def autokey():
            # Creating the fillers for auto key

            if len(args.key) < len(args.plaintext):
                # modulo won't work here so use remainder instead
                # patchvalue=int(math.remainder(len(plainText),len(key)))
                # for i in range(0,1):
                patchvalue = len(args.plaintext) - len(args.key)

                patch = args.plaintext[:patchvalue]
                auto_key = args.key + patch
            elif len(args.key) == len(args.plaintext):
                auto_key = args.key

            # join didn't work so use replace with quotations with a space as first argument and one
            # without as second
            autokey_Mod = auto_key.replace(" ", "")
            print(autokey_Mod.upper())

            def cipher(plaintext, autokey_Mod):
                autokey_mod = autokey_Mod.upper()

                ''' #Encryption algorithm is Ct = (Pt+Ak)mod 26
                 plainText.replace(" ","")
                 Pt = ""
                 #This code is supposed to take the plaintext and convert to corresponding number in
                 #dictionary do the sum and then return result
                 for key in Letters:

                     # pt1= Letters[plainText[i]]
                      #pt2=Letters[autokey_Mod[i]]
                     # Ct1=(pt1+pt2)%26
                     # print(Ct1)
                      #print(Letters[plainText[value]])
                      for value in autokey_Mod:
                       print(Letters[key])'''
                plainText_Mod = plaintext.replace(" ", "")
                plaintext_mod = plainText_Mod.upper()
                ciphertext = ""
                cipherList = []
                for i, char in enumerate(plaintext_mod):

                    if char.isalpha():
                        pt = int(Letters[char])

                        ak = int(Letters[autokey_mod[i]])

                        ct = (pt + ak) % 26

                        print(ct)
                        cipherList.append(ct)

                        '''for letter,num in Letters.items():
                             if num == ct:
                                  ciphertext+= letter
                             else:
                                  ciphertext+=char'''
                        # ct2+=ct

                        # for num in ct:
                        # for key,value in Letters.items():
                        # if value==num:
                        #  print(key)

                        # for num in str(ct):

                        # ciphertext+=Letters[num]

                print(cipherList)
                ciphertext = ""
                for index in range(len(cipherList)):
                    num = cipherList[index]
                    for key, value in Letters.items():
                        if value == num:
                            print(key)
                            ciphertext += key

                print("Ciphertext: ", ciphertext)

            cipher(plaintext, autokey_Mod)

        autokey()

    encryption()


if __name__ == "__main__":
    main()

###Caesar Cipher###

#counting the position of letter in alphabet
def find_letter(split_word):
    global i
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for n in range(26):
        if split_word == letter[n]:
            i = n
    return i

#encryption
def encrypt(word, key):
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    ciphered_word = ""

    for n in word:
        if n.isalpha():
            #converting all letter to lowercase
            lower_n = n.lower()
            for m in range(26):
                if lower_n == letter[m]:
                    i = find_letter(lower_n)
                    if i+key >= 26:
                        #case key overload, circle loop
                        overload = i+key - 26
                        ciphered_word += letter[int(overload)]
                    else:
                        #maintaining the initial state of letter(lower/upper)
                        if n.isupper():
                            letter_upper = letter[i + int(key)].upper()
                            ciphered_word += letter_upper
                        else:
                            ciphered_word += letter[i + int(key)]
        else:
            #no encryption for 'space', special characters & numbers
            ciphered_word += n

    return ciphered_word

#decryption
def decrypt(word, key):
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    ciphered_word = ""

    for n in word:
        if n.isalpha():
            #converting all letter to lowercase
            lower_n = n.lower()
            for m in range(26):
                if lower_n == letter[m]:
                    i = find_letter(lower_n)
                    if i - key < 0:
                        #case key overload, circle loop
                        overload = i - key + 26
                        ciphered_word += letter[int(overload)]
                    else:
                       #maintaining initial state of letter(lower/upper)
                        if n.isupper():                            
                            letter_upper = letter[i - int(key)].upper()
                            ciphered_word += letter_upper
                        else:
                            ciphered_word += letter[i - int(key)]
        else:
            #no encryption for 'space', special char & numeric
            ciphered_word += n

    return ciphered_word

#check whether key is valid
def check_key(key):
    while key.isnumeric() == False or (int(key) > 26 or int(key) < 0):
        print("Please insert number between (0-26) only.")
        key = input("Key: ")

    return key

###START OF PROGRAM###
print("This is an encryption application. Caesar Encryption is applied")
#sen value for loop termination
sen = 1

while sen >= 0 :
    process = input("Please choose between encode(1) and decode(2).\nYou can exit by pressing 'E'.\n")

    if process == '1':
        word = input("Please insert a word: ")
        key = input("Key: ")
        passed_key = check_key(key)

        print(f"Encrypted word: {encrypt(word, int(passed_key))}")

    elif process == '2':
        word = input("Please insert a word: ")
        key = input("Key: ")
        passed_key = check_key(key)

        print(f"Decrypted word: {decrypt(word,int(passed_key))}")

    elif process == 'e' or process == 'E':
        #when sen<0 loop end
        sen = -1

    else:
        print("Option you chose has no operation. Please try again.")
        print("////////////////////////////////////////////////////")

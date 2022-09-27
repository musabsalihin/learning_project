###FUNCTION WITH ARGUMENTS###
###Caesar Cipher###
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def find_letter(split_word):
    global i

    for n in range(26):
        if split_word == letter[n]:
            i = n
    return i

def encrypt(word, key):
    ciphered_word = ""
    for n in word:
        if n.isalpha():
            lower_n = n.lower()
            for m in range(26):
                if lower_n == letter[m]:
                    i = find_letter(lower_n)
                    if i+key >= 26:
                        overload = i+key - 26
                        ciphered_word += letter[int(overload)]
                    else:
                        if n.isupper():
                            letter_upper = letter[i + int(key)].upper()
                            ciphered_word += letter_upper
                        else:
                            ciphered_word += letter[i + int(key)]
        else:
            ciphered_word += n

    return ciphered_word


def decrypt(word, key):
    ciphered_word = ""
    for n in word:
        if n.isalpha():
            lower_n = n.lower()
            for m in range(26):
                if lower_n == letter[m]:
                    i = find_letter(lower_n)
                    if i - key < 0:
                        overload = i - key + 26
                        ciphered_word += letter[int(overload)]
                    else:
                        if n.isupper():
                            letter_upper = letter[i - int(key)].upper()
                            ciphered_word += letter_upper
                        else:
                            ciphered_word += letter[i - int(key)]
        else:
            ciphered_word += n

    return ciphered_word

def check_key(key):
    while key.isnumeric() == False:
        print("Please insert number only.")
        key = input("Key: ")

    return key

print("This is an encryption application. Caesar Encryption is applied")
sen = 1
while sen >= 0 :
    process = input("Please choose between encryption(1) and decryption(2).\nYou can exit by pressing 'E'.\n")

    if process == '1':
        word = input("Please insert a word: ")
        key = input("Key: ")
        passed_key = check_key(key)
        passed_key =  int(passed_key) % 26

        print(f"Encrypted word: {encrypt(word, int(passed_key))}")

    elif process == '2':
        word = input("Please insert a word: ")
        key = input("Key: ")
        passed_key = check_key(key)

        print(f"Decrypted word: {decrypt(word,int(passed_key))}")

    elif process == 'e' or process == 'E':
        sen = -1

    else:
        print("Option you chose has no operation. Please try again.")
        print("////////////////////////////////////////////////////")
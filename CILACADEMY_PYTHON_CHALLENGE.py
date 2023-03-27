import time

# fDECRYPT FUNCTION


def decrypt(ciphertext, key):
    """This function is created to decrypt the cipher text"""
    plaintext = ""
    for i in range(0, len(ciphertext), key+1):
        character = ciphertext[i]
        plaintext = plaintext + character
    return plaintext


ciphertext = input("Kindly enter a message to decrypt the text: ")
key_num = int(input("Kindly input a key between 1 and 10: "))
while (key_num < 1 and key_num > 10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))
print("...")
time.sleep(1)
print("Decrypting ciphertext...")
time.sleep(1)
print("...")
time.sleep(1)
plain_text = decrypt(ciphertext, key_num)
print(f"Decrypted Text: {plain_text}")

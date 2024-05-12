import string

continue_variable = True

while continue_variable:
    direction = input("Type 'encode' or 'decode': ").lower()
    alphabets = string.ascii_lowercase + string.punctuation + string.digits
    text = input("Enter the text: ").lower()
    shift = int(input("Enter the shift amount: "))

    def encrypt():
        cipher_text = ""
        for char in text:
            if char in alphabets:
                position = alphabets.index(char)
                new_position = (position + shift) % len(alphabets)
                cipher_text += alphabets[new_position]
            else:
                cipher_text += char
        print(f"The encoded text is: {cipher_text}")

    def decrypt():
        decrypted_text = ""
        for char in text:
            if char in alphabets:
                position = alphabets.index(char)
                new_position = (position - shift) % len(alphabets)
                decrypted_text += alphabets[new_position]
            else:
                decrypted_text += char
        print(f"The decoded text is: {decrypted_text}")

    if direction == "encode":
        encrypt()
    elif direction == "decode":
        decrypt()
    else:
        print("Invalid choice. Please type 'encode' or 'decode'.")

    again = input("Do you want to encode or decode another text? (yes/no): ").lower()
    continue_variable =="yes"
    if again == "no":
        continue_variable = False
        print("Thank you for using the Caesar Cipher.")
        

from email.quoprimime import decode

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(functionality, original_text, shift_amount):
    if functionality == "decode":
        decrypted_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
        print(f"Here is the decoded result: {decrypted_text}")

    elif functionality == "encode":
        cipher_text = ""
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")

    else:
        print("Please make the right choice")

caesar(functionality=direction, original_text=text, shift_amount=shift)




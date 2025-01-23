from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text: str, shift_amount: int) -> str:
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_number = alphabet.index(letter) + shift_amount

            if shifted_number > 25:
                 # if the number is z then it will encoded to the 9th element in the alphabet array that is j
                encrypted_text += alphabet[shifted_number - 26]
            else:
                encrypted_text += alphabet[shifted_number]
        else:
            encrypted_text += letter

    return encrypted_text

def decrypt(encrypted_text: str, shift_amount: int) -> str:
    decrypted_text = ""
    for letter in encrypted_text:
        if letter in alphabet:
            backward_shifted_position = alphabet.index(letter) - shift_amount
            if backward_shifted_position >= 0:
                decrypted_text += alphabet[backward_shifted_position]
            else:
                decrypted_text += alphabet[26 + backward_shifted_position]
        else:
            decrypted_text += letter

    return decrypted_text


if direction == "encode":
    print(f"Here is the encoded result: {encrypt(text, shift)}")
else:
    print(f"Here is the decoded result: {decrypt(text, shift)}")
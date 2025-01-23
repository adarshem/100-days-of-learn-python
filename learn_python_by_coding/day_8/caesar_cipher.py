alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

def encrypt(original_text: str, shift_amount: int) -> str:
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_number = alphabet.index(letter) + shift_amount

            if shifted_number > 25:
                encrypted_text += alphabet[shifted_number - 25] # if the number is z then it will encoded to the 9th element in the alphabet array that is j
            else:
                encrypted_text += alphabet[shifted_number]
        else:
            encrypted_text += letter

    return encrypted_text

print(encrypt(text, shift))

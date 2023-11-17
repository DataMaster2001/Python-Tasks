#importing necessary libraries
import random

#generates a random number between 1-26
number_generator = random.randint(1,26)

#message that will get ceasar-ciphered
message = 'Version Control is fun'

#function that uses the caesar cypher to encrypt message
def caesar_cypher(message, number_generator):
    encrypted_message = ''

    for letter in message:
        if letter.isalpha():
            start = ord('a') if letter.islower() else ord('A')
            encrypted_message += chr((ord(letter) - start + number_generator) % 26 + start)
        else:
            encrypted_message += letter
        
    return encrypted_message

#encoding the message
encoded_message = caesar_cypher(message, number_generator)

#testing
print(f'original: {message}')
print(f'shifted/number generated: {number_generator}')
print(f'encrypted version: {encoded_message}')


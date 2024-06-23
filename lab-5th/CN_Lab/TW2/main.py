import random
import math
from math import gcd

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# Function to generate random prime numbers
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

# Function to find the modular multiplicative inverse
def mod_inverse(a, m):
    return pow(a, -1, m)

# Function to generate RSA key pairs
def generate_key_pair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
   
    d = mod_inverse(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


# Function to encrypt a message
def encrypt(public_key, message):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text


# Function to decrypt a message
def decrypt(private_key, cipher_text):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return decrypted_message


# Main program
if __name__ == "__main__":
    bits = 8  # Adjust the number of bits for your desired security level
    public_key, private_key = generate_key_pair(bits)
    print(f" Generated Public Key : {public_key} \n Generated Private Key : {private_key}")
    message = input(" Enter the Message to be Encrypted : ")
    print(" Original message:", message)
    encrypted_message = encrypt(public_key, message)
    print(" Encrypted message:", encrypted_message)
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)
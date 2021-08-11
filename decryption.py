message_to_decrypt = input("Enter the encrypted code (just numbers and commas, no square brackets): ")
cipher_to_int = list(map(int, message_to_decrypt.split(",")))


# Start with a pair of prime numbers; p (>=13) and q (>=17)
p = 13
q = 17

# Number n = p * q. n = 221 The function phi(n) = (p-1)*(q-1). phi(n) = 192
n = p * q
phi = (p-1)*(q-1)

#e needs to be greater than 1 but less than phi. phi cannot be divisible by e. 192/5 = 38.4
e = 5

#public key is two values: n = 221 and e = 5. 
#private key d = (i * phi + 1)/e where i is any int. For simplicity, let's say i = 4
i = 2
d =int(((i * phi) + 1)/e)

#repeating the encryption_dict, I could not figure out how to import it from encryption.py
encryption_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E': 5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z': 26, ' ':27, '.':28, "\'":29, ',':30, '!': 31, '?' : 32} 

#Decrypt using a private key
# decrypted = c^d mod n

def decrypt(list):
    '''
    The argument is the list of numbers to be decrypted.
    
    We loop through the numbers in the list applying the decryption equation.
    
    We loop through the encryption_dict items and if the value matches the result of the decryption equation, we add the corresponding key to the empty string and print it.
    '''
    num_to_string = ''
    
    
    for number in list:
        each_num = (number ** d)%n
        for letter, number in encryption_dict.items():
            if number == each_num:
                num_to_string += letter
    print(num_to_string)
    
#Calling the decryption function with the cipher_to_int list from line 4
decrypt(cipher_to_int)
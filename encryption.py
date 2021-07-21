message_to_encrypt = input("Please enter the message to encrypt:")

# Creating an RSA key pair

# Start with a pair of prime numbers; p (>=13) and q (>=17)
p = 13
q = 17

# Number n = p * q. n = 221 The function phi(n) = (p-1)*(q-1). phi(n) = 192
n = p * q
phi = (p-1)*(q-1)

#e needs to be greater than 1 but less than phi. phi cannot be divisible by e. 192/5 = 38.4
e = 5

#public key is two values: n = 221 and e = 5. 

#Encryption using a public key

# The cipher c (the encrypted version of the text) is calculated by:
    #1: Assigning each letter of the message a number. For this example, we're using each letter's position in the alphabet
    #2: Apply the encoding formula to the resulting sequence of numbers
    #*Stick to only lowercase of only uppercase letters to reduce complexity of the program
    
encryption_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E': 5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z': 26, ' ':27, '.':28, "\'":29, ',':30, '!': 31} 

#Function that takes in a string, and converts it to a list of numbers
def translate_string(string):
    '''
    Function takes in a string and makes it uppercase.
    
    We iterate over the uppercase string in the for loop, matching each letter to a number based on the encryption_dict.
    The number has the cipher equation applied to it, resulting in a new number appended into the empty list string_to_num.
    
    We print the list of ciphered numbers.
    '''
    uppercase = string.upper()
    
    string_to_num = []
    
    for letter in uppercase:
        each_lett = encryption_dict[letter]
        cipher = (each_lett ** e)%n #Now, I need to apply the encoding formula (c = translation ^ e mod n) to the resulting sequence of numbers
        string_to_num.append(cipher)
    print(string_to_num)
    
# Call the function with message_to_encrypt
translate_string(message_to_encrypt)
    
import random

print('Welcome to Sarvess Password Generator Program')

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Insert Your Password length: ')
length = int(length)

print('\nhere are your passwords:  ')

for pwd in range(number):
    password = ''
    for c in range(length):
        password  += random.choice(char)
        print (password)
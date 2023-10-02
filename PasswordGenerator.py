#!/usr/bin/python3

import random

length=int(input('Enter your password lenght:  '))
password = ''

for i in range(length):
    choose_ascii = random.randint(33, 126)
    character = chr(choose_ascii)
    password = password + character

print(password)

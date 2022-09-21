#!/usr/bin/python3
for digit in range(89):
    if digit / 10 < digit % 10:
        print('{:02d}'.format(digit), end=", ")
print('{:02d}'.format(digit+1))

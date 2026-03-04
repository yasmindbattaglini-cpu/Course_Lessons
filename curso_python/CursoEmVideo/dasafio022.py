"""Create a new program that read the full name of a person and shows:
a) The full name with upper letters
b) The full name with lower letters
c) How many letters has (without count the spaces)
d) How many letter the first name has"""

name = str(input('Insert your full name: '))

# Full name with upper letters
print(name.upper())

# Full name with lower letters
print(name.lower())

# How many letter has
print('The total of letter you have in your name is: {}'.format(len(name)))

# How many letter you have in first name
print('Your first name has {} letters!'.format(len(name.split()[0])))
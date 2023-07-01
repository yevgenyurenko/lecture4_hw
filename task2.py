number = input('Please input a phone number: ')
if number.isdigit() and len(number)==10:
    print('The number is valid')
else:
    print('Wrong number')
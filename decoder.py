#Theodore Stronkowsky IV
#I was not able to get in contact with my lab partner please take this into account when grading

x = 0
while True:

    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')



    choice = int(input('Please enter an option: '))

    if choice == 1:
        x = int(input('Please enter your password to encode: '))
        x =str(x)
        print('Your password has been encoded and stored!')
        print('')

    if choice == 2:
       a = str((int(x[0]) + 3)%10)
       b = str((int(x[1]) + 3)%10)
       c = str((int(x[2]) + 3)%10)
       d = str((int(x[3]) + 3)%10)
       e = str((int(x[4]) + 3)%10)
       f = str((int(x[5]) + 3)%10)
       g = str((int(x[6]) + 3)%10)
       h = str((int(x[7]) + 3)%10)
       y = a + b + c + d + e + f + g + h
       print(f'The encoded password is {y}, and the original password is {x}.')
       print('')

    if choice == 3:
        break
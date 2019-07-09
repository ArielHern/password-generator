from generator import Password

print('************************************')
print('\t\tWelcome')
print('\nPlease select the type of password')
print('     1.Simple Password')
print('     2.Strong Password')
print('     3.Very Strong Password')


select = int(input())
if select:
    password = Password()
    if select == 1:
        passwrd = password.simplePass()
    elif select == 2:
        passwrd = password.strongPass()
    elif select == 3:
        passwrd = password.superStrongPass()
    else:
        print('Wrong input')
    print('password: ' + passwrd)

from generator import Password


def printer():
    print('     1.Simple Password')
    print('     2.Strong Password')
    print('     3.Very Strong Password')


def pass_gen(passwrd_type):
    try:
        password = Password()
        if passwrd_type == 1:
            passwrd = password.simplePass()
        elif passwrd_type == 2:
            passwrd = password.strongPass()
        elif passwrd_type == 3:
            passwrd = password.superStrongPass()

        print(f'New Password: {passwrd}')
    except Exception as e:
        print('Wrong input')
        printer()
        print('Try Again!')


print('************************************')
print('\t\tWelcome')
print('\t\t  to')
print('\tSimple Password Generator')
print('************************************')
print('\nPlease select the type of password')
printer()

passwrd_type = int(input())
pass_gen(passwrd_type)

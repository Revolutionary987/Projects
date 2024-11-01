
""" Note that password should contain min 8 letters , and atleast one special characters,capital letter ,small letter,digit"""
def password_strength():

    password = input('Please enter your password:')
    return password

def password_checker(password):
    
    if len(password)<8:
        print("Your password must be at least 8 characters long.")

    if  not any(char.isupper() for char in password):
        print("Weak password")
        return False
    if not any(char.isdigit() for char in password):
        print("Weak password")
        return False
    if not any(char.islower() for char in password):
        print("Weak password")
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        print("Weak password")
        return False
    print('Your password is strong enough to be used.')

password=password_strength()

password_checker(password)
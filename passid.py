import random
import string

def generate_password(pass_len):
    password = ""

    for _ in range(pass_len // 3):
        password += random.choice(string.digits)

    for _ in range(pass_len // 3):
        password += random.choice(string.punctuation)

    for _ in range(pass_len - pass_len // 3 * 2):
        password += random.choice(string.ascii_letters)

    return password

pass_no = int(input("Enter the number of passwords you want: "))
pass_len = int(input("Enter your password length: "))

for _ in range(pass_no):
    password = generate_password(pass_len)
    shuffled_password = ''.join(random.sample(password, len(password)))
    
    print("Your password Is:", shuffled_password)

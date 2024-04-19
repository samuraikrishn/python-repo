import random
import string
import time

numbers= string.digits
small_alphabets= string.ascii_lowercase
capital_alphabets= string.ascii_uppercase
special_characters= string.punctuation


while True:
    a=""
    b=""
    print("Welcome to this wonderful password generator")
    print("Do you want to genrate a strong passwword or a weak password(option 1 or 2)")
    try:

        c=int(input("""                Enter 1 for strong password
                Enter 2 for weak password
                Enetr option 3 for exit
                Enter your option::"""))
        if c== 1:
            a+= ''.join(random.sample(small_alphabets,4))
            a+= ''.join(random.sample(capital_alphabets,3))
            a+= ''.join(random.sample(numbers,3))
            a+= ''.join(random.sample(special_characters,4))
            shuffle_a= ''.join(random.sample(a, len(a)))
            for i in range(0,3):
                print("Please wait while we are genrationg your password........")
                time.sleep(1)
            print("Here is your strong password::",shuffle_a)
            
            print()

        elif c==2:
            b+= ''.join(random.sample(small_alphabets,4))
            b+= ''.join(random.sample(numbers,3))
            b+= ''.join(random.sample(capital_alphabets,3))
            shuffle_b= ''.join(random.sample(b, len(b)))
            for i in range(0,3):
                print("Please wait while we are genrationg your password........")
                time.sleep(1)
            print("Here is your weak password::",shuffle_b)
            
            print()
            print("TIP:-If you still want you can change the password")
            print()

        elif c==3:
            for i in range(0,3):
                print("Please wait...while we are exiting.")
                time.sleep(1)
            print("It's been great to genrate a password for you")
            break
    except:
        print("PLease enter valid integer")


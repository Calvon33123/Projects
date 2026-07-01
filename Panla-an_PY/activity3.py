correct_password = "cctc"
attempts =3
name = str(input("Input your name Here: "))
i = "Incorrect Password"

while True:
    password = input("Enter Password: ")
    if password == correct_password:
        print("Welcome")
        break
    
    elif password != correct_password:
        i = 1
        while i <= 3:
            password = str(input("Try Again: "))
            if password == correct_password:
                print("Welcome")
                break
            i =+ 1
            elif password != correct_password:
                password = str(input("Incorrect: "))
                if password == correct_password:
                print("Welcome")
                break
            i =+ 1
    else i == 3:


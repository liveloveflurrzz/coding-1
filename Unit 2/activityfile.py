def passwordReset():
    correctPassword = "secret123"
    attempts = 0
    print("WELCOME TO THE PASSWORD RESET FUNCTION")
    print("Please type in your current password")
    userPassword = input("Please type in your password: ")
    while userPassword != correctPassword and attempts < 4:
        print("Sorry, incorrect. Please try again.")
        attempts += 1
        userPassword = input("Please type in your password: ")
    if userPassword == correctPassword:
        print("Congrats! You can now access your account.")
    else:
        print("Sorry, your account has been locked.")

passwordReset()
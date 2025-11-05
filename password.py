systempassword="1234"
attemptsleft=3

while attemptsleft>0:
    userpassword = input("Enter your login password: ")

    if userpassword == systempassword:
        print("login sucessfull")
        break
    else:
        attemptsleft-=1
        if attemptsleft>0:
            print(f"login failed :{attemptsleft} attemptsleft")
        else:
            print(f"login failed : Account blocked")




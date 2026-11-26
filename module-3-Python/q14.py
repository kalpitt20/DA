# Q14: Login system

user, pwd = "admin", "pass123"
attempts = 0
while attempts < 3:
    u = input("Username: ")
    p = input("Password: ")
    if u == user and p == pwd:
        print("Login Successful")
        break
    attempts += 1
    print("Wrong credentials. Attempts left:", 3 - attempts)
else:
    print("Account Locked")

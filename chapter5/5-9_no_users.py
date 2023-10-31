# user_names = ["aaron", "admin", "bob", "conrad", "doyle", "smuck"]
user_names = []
if user_names:
    for user in user_names:
        if user == "admin":
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print("Hello there!")
else:
    print("We need to find some users")

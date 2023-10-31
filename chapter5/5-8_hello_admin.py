user_names = ["aaron", "admin", "bob", "conrad", "doyle", "smuck"]

for user in user_names:
    if user == "admin":
        print(f"Hello {user.title()}, would you like to see a status report?")
    else:
        print("Hello there!")

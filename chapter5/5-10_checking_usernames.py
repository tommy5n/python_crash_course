current_users = ["aaron", "admin", "bob", "conrad", "Doyle", "smuck"]
new_users = ["axel", "adele", "Bob", "conan", "Doyle", "stig"]

current_users_lower = [user.lower() for user in current_users]
new_users_lower = [new.lower() for new in new_users]

for new_user in new_users_lower:
    if new_user in current_users_lower:
        print("You need to choose another username")
    else:
        print("The username is available")

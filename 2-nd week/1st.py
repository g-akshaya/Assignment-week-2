# Initial user data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# CREATE
def add_user(users, user_id, name, email):
    users.append({"id": user_id, "name": name, "email": email})
    print(f"User with ID {user_id} added.")

# READ
def get_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# UPDATE
def update_user(users, user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print(f"User with ID {user_id} updated.")
            return
    print(f"User with ID {user_id} not found.")

# DELETE
def delete_user(users, user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            print(f"User with ID {user_id} deleted.")
            return
    print(f"User with ID {user_id} not found.")

# Example usage
add_user(users, 3, "Charlie", "charlie@example.com")
print(get_user(users, 2))
update_user(users, 1, name="Alice Smith")
delete_user(users, 2)

# To verify final state of users list
print("Final Users List:", users)

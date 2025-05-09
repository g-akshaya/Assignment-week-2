import hashlib

# Dictionary to store user credentials
user_db = {}

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register function
def register(username, password):
    if username in user_db:
        print("User already exists.")
    else:
        user_db[username] = hash_password(password)
        print("Created new user")

# Login function
def login(username, password):
    hashed = hash_password(password)
    if username in user_db and user_db[username] == hashed:
        print("Login Successful")
    else:
        print("Invalid username or password")


register("john", "mypassword")  # Output: Created new user
login("john", "mypassword")     # Output: Login Successful


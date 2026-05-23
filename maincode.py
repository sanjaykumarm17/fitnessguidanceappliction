import json

#-----Simple Database-----

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return{}
    
def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f)

#------Register-----

def register():
    users = load_users()
    username = input("Enter username: ")

    if username in users:
        print("username already exixts!")
        return None
    
    password = input("Enter password: ")
    users[username] = password
    save_users(users)

    print("Registration Successfull!")
    return username

#-------Login------

def login():
    users = load_users()
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("Login successful !")
        return username
    else: 
        print("Invalid User !")
        return None
    
    

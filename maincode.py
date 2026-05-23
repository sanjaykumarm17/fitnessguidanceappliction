<<<<<<< HEAD
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

#------BMI------

def calculate_bmi():
    weight = float(input("Enter Your Weight (KG): "))
    height = float(input("Enter Your Height (CM): 0")) / 100

    bmi = weight / (height ** 2)

    print(f" Your BMI is: {round(bmi, 2)}")
    
    if bmi < 45:
        print("You're Underweight")
    elif bmi < 70:
        print("You're Normalweight")
    elif bmi < 100:
        print("You're Overweight")
    else:
        print("obese")

#-------Workout------

def workout_plan():
    print("\nSelect Goal: ")
    print("1. Fat Loss")
    print("2. Muscle Gain")
    choice = input("Enter choice: ")

    if choice == "1":
        print("\nWorkout Plan for Fat Loss:")
        print("- 5km to 7Km Walking")
        print("- 3minutes of Skipping --- 3 Sets")
        print("- 20 Squats --- 3 Sets")
        print("-15 Push-ups --- 3 sets")
        print("- 5minutes of Full-Body Stretch")
    elif choice == "2":
        print("\nWorkout Plan for Muscle Gain:")
        print("- 3minutes Full-Body Stretch")
        print("-20 Push-ups --- 3 Sets")
        print("-15 Pull-ups --- 3 Sets")
        print("- Weight Training")
    else:
        print("Invalid Choice !")

#--------Diet------

def diet_plan():
    print

    
        
=======

>>>>>>> 3747676466ab7fda3923bbc56b3c60bcedf6be68

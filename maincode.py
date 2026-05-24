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
choice = input("Enter the choice: ")

def diet_plan():
    if diet_plan == "1":
        print("\nDiet Plan for Fat Loss: ")
        print("- Rice / chapati")
        print("- Vegetables")
        print("- white Egg / Protein")
        print("- Fruits")
        print("- Drink Water")
    elif diet_plan == "2":
        print("\nDiet Plan for Muscle Gain: ")
        print("- 250 kgm Chicken")
        print("- Vegetables")
        print("- Full egg / protein")
        print("- Milk")
        print("- Drink Water")

#--------Main APP-------

"REGISTER"
"LOGIN"
"CALCULATE THE BMI"
"WORKOUT PLAN"
"DEIT PLAN"
"LOGOUT"

#---------------------------

def fitness_app():
    while True:
        print("\n==== Fitness App =====")
        print("1. Reigter")
        print("2. Login")
        print("3. calculate BMI")
        print("4. Workout Plan")
        print("5. Deit Plan")
        print("6. Logout")
        print("7. Exit")

        choice = input("Enter the choice: ")

        if choice == "1":
            user = register()
            if user:
                fitness_app(user)

        elif choice == "2":
            user = login()
            if user:
                fitness_app(user)

        elif choice == "3":
            calculate_bmi()
        elif choice == "4":
            workout_plan()
        elif choice == "5":
            diet_plan()
        elif choice == "6":
            print("Logged Out !")
        elif choice == "7":
            print("Exit")
            break
        else:
            print("Invalid choice !")

if __name__ == "__fitness_app":
    fitness_app()
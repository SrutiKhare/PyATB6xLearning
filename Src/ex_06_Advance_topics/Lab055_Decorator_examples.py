def add_security(func):
    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcash, gloves,knee guard")
        func()
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")

    return wrapper

    return wrapper
@add_security
def driveOla_Scooter():
    print("I am driving the ola scooter")

@add_security
def driveZepp_Scooter():
    print("I am driving the Zepp scooter")

driveZepp_Scooter()
print("\n")
driveOla_Scooter()


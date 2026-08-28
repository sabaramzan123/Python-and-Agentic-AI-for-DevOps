print("Hello, World!")

#variables
name = "Saba"
age = 24
no_of_env = 3

#data types = > int, float, str, bool, list, tuple, dict

print(type(no_of_env))
print(type(name))

#data structures -> list, dict, tuple, set
env = ["dev", "stage", "prod"]
print(type(env))

info = {
    "name": "Saba",
    "age": 24,
    "years_of_experience": 1,
    "env": ["dev", "stage", "prod"]
}

print(info["years_of_experience"]) #dictonary
print(type(info))

#tuple -> immutable, cannot be changed, ordered
days_of_week = ("Monday", "tuesday", "wednesday", "thurs", "fri", "sat", "sun")
print(type(days_of_week))
print(days_of_week[1])

#set => gives unique values
num = {0, 1, 4, 5,3, 4, 7,7, 9, 9}
print(num)
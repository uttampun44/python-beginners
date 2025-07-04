fruits = ['apple', 'banana', 'orange', 'mango', 'grape', 'strawberry']

for i in range(len(fruits)):
    print(fruits[i])

# list
person_details = []
person_name = input("Enter your name: ")
person_age = int(input("Enter your age: "))
person_email = input("Enter your email: ")

# dictionary
person_Details = {
    'name': person_name,
    'age': person_age,
    'email': person_email
}
person_details.append(person_Details)

print(person_Details)
student = {"name" : "Asha", "fee" : 2000, "paid" : 1500}

print(student.get("email", "no email"))


print(student["email"])
#Traceback (most recent call last):
#print(student["email"])
#KeyError: 'email'

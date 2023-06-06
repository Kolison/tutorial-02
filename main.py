is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

if is_admin or is_permission == True:
    result = is_active == True
    result = is_permission == True
    print: ("Welcome")
else: 
    print (0)
access = True
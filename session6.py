# تخفیف
for i in range(0,5):
    price=int(input('Enter a price: '))
    if price<100:
        print(price)
    else:
        print(price-price/10)
        
#مثلث خیام
n = int(input("Enter number of rows: "))
for i in range(1, n+1):
    for j in range(i):
        print(1, end=" ")
    print()

#اسامی 
names = ["ali", "sara", "maziyar", "mohammad", "abolfazl"]
for name in names:
    if len(name) < 5:
        continue
    print(f"Valid name found: {name}")

#فاکتوریل
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i
    
print(f"factorial of {number} is: {factorial}")

###############################################################

#Dictionary
user={
  'username':'Maziyar',
  'password':'a123',
  'email':'Maziyar@gmail.com',
  'age':23,
  'isTeacher':True
}

print(user)
print(type(user))
print(user['email'])

#value types
user1={
  'username':'Maziyar',
  'password':'a123'
}
user2={
  'username':'amir',
  'password':'zzz111'
}
username,password=input("please enter username: "),input("please enter password: ")
if username==user1['username'] and password==user1['password']:
  print("login user1")
elif username==user2['username'] and password==user2['password']:
  print('login user2')
else:
  print("Error")

student={
  'name':'adabi',
  'nc':'7788',
  'schoolName':'alghadir',
  'age':23
}
#modify/edit
student['schoolName']='tizhoshan'
print(student)

#add key,value
student['number']=9111
print(student)

#delete
del student['nc']
print(student)

#Pop
deletedValue=student.pop('nc')
print(deletedValue)
print(student)

#deletes last item
deletedValue=student.popitem()
print(deletedValue)
print(student)

#get in dictionary
#if i type print(student['shirtColors']) i get error so i use get
message1=student.get('shirtColor','we dont have this key')
message2=student.get('schoolName','we dont have this key')
print(message1)
print(message2)

#show all
print(student.items())
for key,value in student.items():
  print(f"{key}--->{value}")

#Show key - show value
print(student.keys())
print(student.values())

#Class
favoriteLanguages={
  'amir':'cpp',
  'ali':'python',
  'mmd':'csharp'
}
print(favoriteLanguages.items()) #key + value
print(favoriteLanguages.keys())
print(favoriteLanguages.values())

#This method gets the keys and values together
for name,language in favoriteLanguages.items():
  print(f"{name.upper()} favorite language is {language.title()}")

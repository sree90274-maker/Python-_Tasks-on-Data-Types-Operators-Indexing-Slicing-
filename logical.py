#Create a student login validation using logical operators.  

username = input("Enter username: ")
password = input("Enter password: ")
valid_user = (username == "student")
valid_pass = (password == "1234")
print(valid_user and valid_pass)   
print(valid_user or valid_pass)    
print(not valid_user) 

# Build a list indexing program to access employee names.  

employees = ["Durga","kayi","sree","tharun"]
print(employees[0])
print(employees[1])
print(employees[2])
print(employees[3])

#Create a program to reverse a string using slicing. 
 
employees = ["Durga", "Bhavya", "nani","tharun"]
reversed_employees = employees[::-1]
print(employees)
print(reversed_employees)    

#Write a program to find even or odd numbers using bitwise operators. 
 
num = int(input("Enter a number: "))
if num&1:
   print("odd number")
else:
   print("even number")   

#Create a list search program using membership operators.  

employees = ["Durga", "Bhavya", "nani","tharun"]
name = input("Enter employee name to search: ")
if name in employees:
   print("Employee found")
else:
   print("Employee not found")

#Write a tuple indexing program for company records. 
 
company = ("TCS","Infosys","Wipro","HCL")
print(company[0])
print(company[1])
print(company[2])
print(company[3])

#Build a mini inventory system using lists and dictionaries. 
 
inventory = {"Laptop":10,"Mouse":50,"Keyboard":30}
print(inventory["Laptop"])
print(inventory["Mouse"])
print(inventory["Keyboard"])
  

  
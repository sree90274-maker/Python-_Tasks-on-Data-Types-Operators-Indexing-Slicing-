#Write a program to identify the data type of user input.  

user_data = input("Enter a value:")
print(type(user_data))

#Create a program using all numeric data types.
#integer data type  
number = 25
print(number)
print(type(number))

#float datatype
phonepay = 200.62
print(phonepay)
print(type(phonepay))

#complex datatype
value = 4 + 2j
print(value)
print(type(value))

print("__________________")

age = 20
weight = 55.5
result = 3 + 4j
print(age)
print(type(age))
print(weight)
print(type(weight))
print(result)
print(type(result))

#Build a shopping bill calculator using arithmetic operators.  
shirt = 500
shoes = 1200
bag = 800
total_bill = shirt + shoes + bag
print(total_bill)

print("___________________________________")

rice = int(input("Enter rice price: "))
oil = int(input("Enter oil price: "))
sugar = int(input("Enter sugar price: "))
total = rice + oil + sugar
discount = total - 100
double_bill = total * 2
average = total / 3
floor_value = total // 3
remainder = total % 3
print(total)
print(discount)
print(double_bill)
print(average)
print(floor_value)
print(remainder)

#Write a program to compare two employee salaries. 
emp_1 = 30000
emp_2 = 25000
if emp_1>emp_2:
    print("Employee 1 salary is higher")
else:
    print("Employee 2 salary is higher") 



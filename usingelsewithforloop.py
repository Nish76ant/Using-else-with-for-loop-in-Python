number1 = int(input("Enter numer for items : \n"))
number2 = input("Enter the type of Comprehensions {list/set/dictionary} \n")

if number2 == 'list':
    t = [i for i in range(number1)]
    print(t)
elif number2 == 'set':
    t = {i for i in range(number1)}
    print(t)
elif number2 == 'dictionary':
    t = {i:f"item{i}"for i in range(number1)}    
    print(t)    
else:
    print('Please enter valid input {set/list/dictionary}')    

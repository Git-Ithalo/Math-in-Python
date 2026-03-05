print("----Welcome to Ithalo's calculator----")
print("Press 1 to add \nPress 2 to decrease \nPress 3 to multiplicate \nPress 4 to divide")
menu =(int(input(("Choice the operation:"))))
operation1= 0
operation2 = 0 
result= 0
if menu == 1:
    operation1 = (float(input("Say your first Number: ")))
    operation2 = (float(input("Say your second Number: ")))
    result = operation1 + operation2
    print("The result is: {}".format(result))
elif menu == 2:
    operation1 = (float(input("Say your first Number: ")))
    operation2 = (float(input("Say your second Number: ")))
    result = operation1 - operation2
    print("The result is: {}".format(result))
elif menu == 3:
     operation1 = (float(input("Say your first Number: ")))
     operation2 = (float(input("Say your second Number: ")))
     result = operation1 * operation2
     print("The result is: {}" .format (result))
elif menu == 4:
    operation1 = (float(input("Say your first Number: ")))
    operation2 = (float(input("Say your second Number: ")))
    result = operation1 / operation2
    print("The result is: {}" .format (result))
else:
    print("Send one right number")
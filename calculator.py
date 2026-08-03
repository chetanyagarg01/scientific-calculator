import functions
ch=1
while ch == 1: 
    print("Select operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exponentiation \n 6. Logarithm \n 7. Square Root \n 8. Factorial \n 9. Trigonometric Functions \n 10. Percentage \n 11. Permutation \n 12. Combination" )
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11/12): ")
    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']: 
        print("Invalid input")
        continue
    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    elif choice in ['5', '6']:
        a = float(input("Enter main number: "))
        b = float(input("Enter power/base number: "))
    elif choice in ['7', '8']:
        a = float(input("Enter number: "))
    elif choice == '9': 
        a = input("Enter trigonometric function (sin/cos/tan): ").strip().lower()
        b = float(input("Enter angle in degrees: "))
    elif choice == '10':
        a = float(input("Enter the number: "))
        b = float(input("Enter the max: "))
    elif choice in ['11', '12']:
        a = int(input("Enter n (total items): "))
        b = int(input("Enter r (items to choose): "))
    if choice == '1':
        print(functions.add(a, b))
    elif choice == '2':
        print(functions.subtract(a, b))
    elif choice == '3':
        print(functions.multiply(a, b))
    elif choice == '4':
        print(functions.divide(a, b))
    elif choice == '5': 
        print(functions.expo(a, b))
    elif choice == '6':
        print(functions.log(a, b))
    elif choice == '7': 
        print(functions.sqrt(a))
    elif choice == '8':
        print(functions.factorial(a))
    elif choice == '9':
        print (functions.trig(a, b))
    elif choice == '10': 
        print (functions.percent(a, b), '%')
    elif choice == '11':
        print (functions.perm(a, b))    
    elif choice == '12':
        print (functions.comb(a, b))
    else:
        print("Invalid input")
    ch = int(input("Do you want to perform another calculation? (1 for Yes / 0 for No): "))
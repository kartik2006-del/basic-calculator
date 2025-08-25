print('-------- welcome to the basic calculator --------'.title().center(120))

num1=float(input('enter your number1 : '))

num2=float(input('enter your number2 : '))

operation=input('enter your operation (+ , - , * , /) : ')

match operation:
    case "+":
        print("Result : ", num1+num2)
    case "-":
        print('Result : ', num1-num2)
    case "*":
        print('Result : ', num1*num2)
    case "/":
        if num2!=0:
            print('Result : ', num1/num2)
        else:
            print('Error ! Division by zero ')
    case _:
        print('invalid operation')


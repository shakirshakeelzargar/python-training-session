# 4. Use Exception handling all above programs.
# 1. Write a program to  find if a number is exactly divisible by 2
def divisibleCheck(n):
    try:
        inputNumber = int(n)
        if inputNumber%2 == 0:
            print('Given number is even')
        else:
            print('Given number is odd')
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')

# divisibleCheck('1')

# 2. Take 4 integers and print the lowest integer value, if all are equal, raise an exception stating all values are equal.
def lowestNumber(a,b,c,d):
    num1,num2,num3,num4 = float(a),float(b),float(c),float(d)
    try:
        if num1 == num2 == num3 == num4:
            raise Exception('Input values are equal')
    except Exception as ex:
        print(f'ERROR: {ex}')
    else:
        if (num1 < num2) and (num1 < num3) and (num1 < num4):
            print(f'Smallest number is: {num1}')
        elif (num2 < num3) and (num2 < num4) and (num2 < num1):
            print(f'Smallest number is: {num2}')
        elif (num3 < num4) and (num3 < num1) and (num3 < num2):
            print(f'Smallest number is: {num3}')
        else:
            print(f'Smallest number is: {num4}')
    finally:
        print('Execution Done.')
# lowestNumber(1.1,1.2,3,4)

# 3. Write a program to reverse an integer
def reverseNumber(n):
    try:
        inputNumber = int(n)
        reverse = 0
        while(inputNumber > 0): 
            remainder = inputNumber % 10
            reverse = reverse * 10 +  remainder
            inputNumber = inputNumber // 10
            print(f'Result:{reverse}') 
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')
# reverseNumber('12345')
  
def doWhileFunction(n):
    try:
        while n:
            n=n-1
            print(n if 0<1 else 1)
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')

# doWhileFunction(1)

def greatestNumber(num1,num2,num3,num4):
    try:
        largeNumber = num1 if (num1 > num2 and num1 > num3 and num1 > num4) else (num2 if (num2 > num3 and num2 > num4) else (num3 if num3 > num4 else num4))
        print(f'Largest number is: {largeNumber}')
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')

# greatestNumber(10, 1, 100, 5)


def primeNumber(start, end):
    try:
        inputNumbers = list(range(start, (end+1)))
        primeNumbers=[n for n in inputNumbers if (n%2 != 0)]
        print(f'Prime Numbers: {primeNumbers}')
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')

# primeNumber(1, 100)

def orderedList(i):
    try:
        newList = []
        inputList = list(set(i))
        while inputList:
            tempMin = inputList[0]
            for num in inputList:
                if num < tempMin:
                    tempMin = num
            newList.append(tempMin)
            inputList.remove(tempMin)  
        return newList
    except Exception as e:
        print(f'Error occured: {e}')

def smallAndLarge(i):
    try:  
        print(f'Smallest Number: {orderedList(i)[0]}')
        print(f'Largest Number: {orderedList(i)[-1]}')
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')

# smallAndLarge([-1, 200, 5, 80, 0, 100, 1])

def ascendingDict(dict):
    try:
        output={value:orderedList(dict[value]) for index,value in enumerate(dict)}
        print(f'Result Object: {output}')
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')

''' ascendingDict({
    "fruits":["mango","apple","banana"],
    "countries":["India","Australia","Bangladesh"]
}) '''


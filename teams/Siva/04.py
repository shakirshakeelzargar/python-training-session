# Write a python function which takes a list as an argument and returns the sum of elements in the list
def addElementInList(inputList):
    try:
        sum, ls = 0, []
        for el in inputList:
            sum += el
        ls.append(sum)
        print(f'Result : {ls}')
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')
        #print(sum([1,2,3,4]))

addElementInList([1,2,3,4,5])

# Create a function which performs the basic arithmatic operations(+,-,/,*). It takes three inputs, num1, num2 and operator symbol as string 

def arithmatic(a, b, operator):
    try:
        if operator == '+':
            reslut=a+b
        elif operator == '-':
            reslut=a-b
        elif operator == '*':
            reslut=a*b
        elif operator == '/':
            reslut=a//b
        print(f'Result : {reslut}')
    except Exception as e:
        print(f'Error occured: {e}')
    finally:
        print('Execution Done.')

# arithmatic(4, 2, '/')

# You are given lengtgh and breadth of a rectangular feild. Create a class which is constructed using length and breadth. The class should contain a method names get_area. Calling this method should return the area of the rectangular feild.

class AreaOfRectangle:
    def __init__(self,l, b):
        print("I am inside init")
        self.lengtgh=l
        self.breadth=b

    def get_area(self):
        return self.lengtgh * self.breadth


# obj=AreaOfRectangle(4, 2)
# print('area of the rectangle : ', obj.get_area())
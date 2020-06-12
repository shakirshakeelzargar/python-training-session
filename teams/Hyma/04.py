# python function for sum of elements in the list

def sum(numbers):
    result = 0
    for number in numbers:
        result = result + number
        
    return result
numbers=[1,2,3]
print(sum(numbers))

#function to perform arithmetic operations

def arithmetic(numberOne, numberTwo, operator):

    return eval(str(numberOne) + operator + str(numberTwo))

print(arithmetic(2,3,'+'))


#Function for finding the area using class

class area:
    length = 2
    breadth = 2
    def getArea():
        return area.length*area.breadth

area.getArea()



def employee(empId):
    
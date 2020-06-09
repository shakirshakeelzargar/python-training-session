#finding the number exactly divisable by 2

number = 5
try:
    if(number%2!=0):
        print("number is not exactly divisable by 2")
except:
    print("please enter the number exactly divisable by 2")


#finding the lowest number

def lowestNumbers(numberOne, numberTwo, numberThree, numberFour):
    try:
        if(numberOne == numberTwo or numberOne == numberThree or numberOne == numberFour or numberTwo == numberThree or numberTwo == numberFour or numberThree == numberFour):
            raise exception("equal numbers found:")
        elif(numberOne < numberTwo and numberOne < numberThree and numberOne < numberFour):
            lowestNumber = numberOne
            print("number one is the lowest number:", lowestNumber)
        elif(numberTwo < numberOne and numberTwo < numberThree and numberTwo < numberFour):
            lowestNumber = numberTwo
            print("number two is the lowest Number:", lowestNumber)
        elif(numberThree < numberOne and numberThree < numberTwo and numberThree < numberFour):
            lowestNumber = numberThree
            print("number three is the lowest Number:", lowestNumber)
        elif(numberFour < numberOne and numberFour < numberTwo and numberFour < numberThree):
            lowestNumber = numberFour
            print("number four is the lowest Number:", lowestNumber)
    except:
        print("exception")   

lowestNumbers(0,1,2,3)

# reverse of a number

number = 34234
numberToString = str(number)
print("revesed number:", int(numberToString[::-1])) 

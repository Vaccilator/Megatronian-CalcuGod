import numbers as n


class Numbers:
    def __init__(self, firstNumber: n.Number, secondNumber: n.Number):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def setFirstNumber(self, firstNumber: n.Number):
        self.firstNumber = firstNumber

    def setFirstNumber(self, secondNumber: n.Number):
        self.secondNumber = secondNumber

    def getFirstNumber(self) -> n.Number:
        return self.firstNumber

    def getSecondNumber(self) -> n.Number:
        return self.firstNumber

firstNumber = float(input('Insert the first number: '))
secondNumber = float(input('Insert the second number: '))

print('Choose the function you would like to use on the numbers.')
print('1.Add 2.Subtract 3.Multiply 4.Divide')

promptResult = int(input('Select the number 1-4: '))

match promptResult:
    case 1:
        calculatorResult = firstNumber + secondNumber
        print(calculatorResult)
    case 2:
        calculatorResult = firstNumber - secondNumber
        print(calculatorResult)
    case 3: 
        calculatorResult = firstNumber * secondNumber
        print(calculatorResult)
    case 4:
        while True:
            if secondNumber == 0:
                print('Error. Division by zero')
                break
            else:
                calculatorResult = firstNumber / secondNumber
                print(calculatorResult)
                break





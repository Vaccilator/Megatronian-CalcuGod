calculatorFirstNumber = int(input('Insert the first number: '))
calculatorSecondNumber = int(input('Insert the second number: '))
print('Choose the function you would like to use on the numbers.')
print('1.Add 2.Subtract 3.Multiply 4.Divide')
calculatorFunctionPromptResult = input('Select the number 1-4: ')

for i in calculatorFunctionPromptResult:
    if calculatorFunctionPromptResult == 1:
        calculatorResult = calculatorFirstNumber + calculatorSecondNumber
        print(calculatorResult)
    elif calculatorFunctionPromptResult == 2:
        calculatorResult = calculatorFirstNumber - calculatorSecondNumber
        print(calculatorResult)
    elif calculatorFunctionPromptResult == 3:
        calculatorResult = calculatorFirstNumber * calculatorSecondNumber
        print(calculatorResult)
    elif calculatorFunctionPromptResult == 4:
        calculatorResult = calculatorFirstNumber / calculatorSecondNumber
        print(calculatorResult)
    else:
        break



from Calculator.evaluation import evaluate
from Calculator.convertor import bases


while True:
    number_system = input('Please, choose your operation. Enter 2, 10, 12 ')
    if number_system in ['2', '10', '12']:
        break
    else:
        print('Enter correct value')

while True:
    value1 = input('Input firts value ')
    if number_system == '10':
        try:
            value1 = float(value1)
            break
        except ValueError:
            print("That was incorect value")
    else:
        value1 = bases.fromBase(value1, int(number_system))
        break

while True:
    value2 = input('Input second value ')
    if number_system == '10':
        try:
            value2 = float(value2)
            break
        except ValueError:
            print("That was incorect value")
    else:
        value2 = bases.fromBase(value2, int(number_system))
        break
    

while True:
    operator = input('Please, choose your operation. Enter *, /, + or - ')
    if operator in ['*', '/', '+', '-']:
        break
    else:
        print('Enter correct value')

result_value = evaluate(value1, value2, operator)
if result_value == None:
    print("Сan't divide by zero")
else:
    result_value = bases.toBase(result_value,int(number_system))
    print(result_value)
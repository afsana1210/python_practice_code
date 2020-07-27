opration=input('would you like to add/substract/multiply/divide : ').lower()

print('you choose{}'.format(opration))

if opration=='substract' or opration=='divide':
    # print('you choose{}'.format(opration))
    print("please keep in mind that order of number is important")

num1=input('what is first number')
num2=input('what is second number')

print('first number is {}'.format(num1))
print('second number is {}'.format(num2))



try:
    num1,num2=float(num1),float(num2)
    if opration=='add':
        result=num1+num2
        print('{}+{}={}'.format(num1,num2,result))
    elif opration=='substract':
        result=num1-num2
        print('{}-{}={}'.format(num1,num2,result))
    elif opration=='Multiply':
        result=num1*num2
        print('{}*{}={}'.format(num1,num2,result))
    elif opration=='divide':
        result=num1/num2
        print('{}/{}={}'.format(num1,num2,result))
    else:
        print('sorry but {} is not an option'.format(opration))
except:
    print('Error improper number used.please try again')




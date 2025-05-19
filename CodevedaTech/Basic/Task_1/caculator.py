def simple_caculator(a,b,operation):
    match(operation):
        case '+':
            return a+b
        case'-':
            return a-b
        case '*':
            return a*b
        case '/': 
            if(b==0):
                return 'Can divide to zero'
            return a/b

            
  

a = float(input('Enter number a: '))
b  = float(input('Enter number b: '))
operation = input('Enter (+,-,*,/) to caculate a and b: ')
result = simple_caculator(a,b,operation)
print(result)
